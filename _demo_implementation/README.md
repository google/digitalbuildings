# DBO in a BMS — a sample implementation

A small, runnable reference for teams putting the [Digital Buildings Ontology](../ontology/README.md)
into a real building management system: what to store when you create a device,
how to map its points, and how location fits in.

It is **not** part of the upstream project and nothing here is authoritative.
It is one worked example of the code you end up writing around DBO, with the
awkward parts left in rather than tidied away.

The generated config passes Google's own instance validator — see
[Proof it works](#proof-it-works).

```
_demo_implementation/
├── README.md                  ← you are here
├── bms_dbo/                   the library
│   ├── ontology.py            read a pinned copy of the DBO
│   ├── models.py              the BMS-side data model
│   ├── naming.py              FACILITIES code conventions
│   ├── loader.py              CSV → model (stands in for your database)
│   ├── type_matcher.py        infer an entity type from a point set
│   ├── mapping_validator.py   offline checks, the fast inner loop
│   ├── exporter.py            model → building_config.yaml
│   ├── webui_render.py        HTML for the dashboard (pure functions)
│   ├── webui.py               the dashboard's HTTP server
│   └── cli.py                 python -m bms_dbo <command>
├── sample_site/               four CSVs = four database tables
├── tests/                     299 tests
├── schema.sql                 the same model as SQL DDL
├── ontology_pin.yaml          which ontology revision we speak
├── ci/validate.sh             the four CI gates
├── bitbucket-pipelines.yml    sample pipeline
└── Makefile
```

## Run it

Python 3.9+ and PyYAML. Nothing else.

```bash
cd _demo_implementation
pip install -r requirements.txt

python -m bms_dbo serve         # a browser dashboard -- click through it
python -m bms_dbo demo          # the same walkthrough, printed to a terminal
```

### The dashboard

`python -m bms_dbo serve` opens `http://127.0.0.1:8765/` in a browser. This
is the answer to "the CLI doesn't feel right for non-BMS people" — click a
device instead of reading `[ERROR]` lines:

* **Dashboard** — the building's `CONTAINS` tree, a device table with a
  clean/warning/issues badge per device, and error/warning counts.
* **A device page** (click any device) — its assigned type and why it fits,
  the ranked type candidates from recommendation #3, every mapped point with
  its unit or link, and the validation findings scoped to that one device.
* **Validate** — the full findings table, colour-coded by severity.
* **Export** — the generated `building_config.yaml`, or a blocked-export
  notice with a link back to the errors if the site isn't clean yet, plus a
  download link.
* **Ontology** — the pin digest, drift status, and the counts from
  `ontology-info`.

It is read-only and stdlib-only: no Flask, no build step, one process. It
**re-reads the CSVs on every request** — edit `sample_site/point_mappings.csv`,
hit refresh, see the new validation result immediately. Point it at your own
data with `--site path/to/your/csvs`, or run headless with `--no-browser`.

### The CLI, one step at a time

| Command | What it shows |
|---|---|
| `python -m bms_dbo ontology-info` | which ontology revision this build speaks |
| `python -m bms_dbo suggest-types` | entity types inferred from each device's points |
| `python -m bms_dbo validate` | every mapping, type and edge checked offline |
| `python -m bms_dbo export` | writes `out/building_config.yaml` |
| `python -m bms_dbo serve` | the browser dashboard above |
| `make test` | the test suite |
| `make ci` | all four gates, the way CI runs them |

Every command above has a `make` shortcut too — run `make help` to list them.

Point any command at your own data with `--site path/to/your/csvs`.

---

## The sample site

A small Melbourne building. Deliberately includes the two shapes that cause
most of the trouble in practice: a **gateway** reporting on behalf of devices
that have no cloud presence of their own, and a device that is **missing a
point its type requires**.

```
AU-MEL-DEMO                          FACILITIES/BUILDING
└── AU-MEL-DEMO-1                    FACILITIES/FLOOR
    ├── AU-MEL-DEMO-1-PLANT          FACILITIES/ROOM
    │   ├── AHU-1                    HVAC/AHU_DFSS_DTC_CHWVM_RTM   reporting
    │   └── GW-1                     GATEWAYS/PASSTHROUGH          reporting
    ├── AU-MEL-DEMO-1-101            FACILITIES/ROOM
    │   └── VAV-L1-01                HVAC/VAV_SD_DSP               virtual → GW-1
    └── AU-MEL-DEMO-1-102            FACILITIES/ROOM
        ├── VAV-L1-02                HVAC/VAV_SD_DSP               virtual → GW-1
        └── FCU-1                    HVAC/FCU_DFSS_CSP_CHWDC       reporting

FEEDS:  AHU-1 → VAV-L1-01, VAV-L1-02
        VAV-L1-01 → room 101,  VAV-L1-02 → room 102,  FCU-1 → room 102
```

`GW-1` translates twelve enumerated points (`zone_air_temperature_sensor_1`,
`…_2`, …). The two VAVs own none of them; each VAV **links** its six standard
fields to the gateway's enumerated ones. That is the pattern most BACnet
supervisor installations need.

---

## The six recommendations, in code

### 1. Store the DBO mapping alongside the native point — not instead of it

One row per `(device, DBO field)`, carrying both sides.

`sample_site/point_mappings.csv`:

```csv
device_code,dbo_field,reporting_field,native_path,native_unit,dbo_unit,native_states,missing,value_min,value_max,missing_justification
AHU-1,discharge_air_temperature_sensor,,points.supply_air_temp.present_value,degC,degrees_celsius,,FALSE,10,30,
AHU-1,discharge_fan_run_command,,points.supply_fan_cmd.present_value,,,ON=active;OFF=inactive,FALSE,,,
```

Note the rename on the first row: the panel calls it `supply_air_temp`, DBO
calls it `discharge_air_temperature_sensor`. DBO reserves `supply` for the
upstream side and `discharge` for what leaves the unit — the opposite of common
BMS convention. Expect a lot of that, and expect to keep both names forever:
`native_path` stays authoritative for polling, `dbo_field` is what analytics
and the exported config read.

Code: [`models.PointMapping`](bms_dbo/models.py), [`schema.sql`](schema.sql)
(`dbo_point_mapping`).

### 2. Vendor the ontology and version-pin it

The DBO gains types continuously — the ASHP additions in this repository's
recent history are a live example. A build that validates against "whatever is
on master today" is not reproducible.

We pin a **content digest** of `ontology/yaml/resources`, not a git revision.
When the ontology is vendored inside the consuming repository a git pin drifts
on every unrelated commit; the digest changes only when the vocabulary does.

```console
$ python -m bms_dbo ontology-info
pinned digest   : 99340171defe834c7bde47824dd33aeccdc66e5f20faf2f96372e26885469ab9
actual digest   : 99340171defe834c7bde47824dd33aeccdc66e5f20faf2f96372e26885469ab9
entity types    : 2627
standard fields : 1537
states          : 67
unit families   : 69
```

Exits non-zero on drift, so CI tells you the vocabulary moved before a customer
does. `make pin` prints the current digest.

Code: [`ontology.ontology_digest`](bms_dbo/ontology.py), [`ontology_pin.yaml`](ontology_pin.yaml).

### 3. Infer the entity type from the mapped points

Nobody should pick from a dropdown of 40 `VAV_SD_DSP_*` variants. Once the
points are mapped, the candidates are computable: a type fits if every field it
*requires* is declared, and fits *well* if it can also express everything else.

```console
$ python -m bms_dbo suggest-types
FCU-1  (7 field(s) declared)
  assigned : HVAC/FCU_DFSS_CSP_CHWDC
             -> exact, canonical
  suggested:
   *1. HVAC/FCU_DFSS_CSP_CHWDC                exact, canonical
    2. HVAC/FCU_DFSS_CHWDC_ZTM                1 point(s) unrepresentable, canonical
    3. HVAC/FCU_DFSS_CSP_CHWZC                1 point(s) unrepresentable, canonical

GW-1  (12 field(s) declared)
  assigned : GATEWAYS/PASSTHROUGH
             -> accepts undefined fields; nothing to infer
```

Ranking, in order: fewest points the type *cannot* express (those would be
silently dropped), then fewest unmet requirements, then prefer canonical, then
the tightest fit. Enumerated names are stripped first, so a gateway's
`zone_air_temperature_sensor_1` matches the same types as the bare field.

This is the `tools/explorer` query — "what types are associated with this field
set?" — with ranking added so a UI can lead with one recommendation.

Code: [`type_matcher.suggest_types`](bms_dbo/type_matcher.py).

### 4. Make `MISSING` a first-class state

A field a type requires but the device cannot supply is declared `MISSING`.
That is valid DBO. **Dropping the row instead fails validation.**

```csv
FCU-1,discharge_air_temperature_setpoint,,,,,,TRUE,,,Controller exposes no discharge setpoint object; ...
```

becomes

```yaml
    discharge_air_temperature_setpoint: MISSING
```

The upstream validator warns and demands an explanation, so the model has a
`missing_justification` column and the validator errors without one:

> You must provide justification for all MISSING translations … otherwise your
> building config will be rejected.

A `MISSING` row also carries no path, unit or range — enforced in both
`PointMapping.validate()` and a `CHECK` constraint in `schema.sql`.

Code: [`models.PointMapping.validate`](bms_dbo/models.py),
[`mapping_validator`](bms_dbo/mapping_validator.py).

### 5. Model location as an edge, from day one

There is no `floor_id` column on a device anywhere in this codebase. Location
is a `CONTAINS` edge in the same table that carries `FEEDS`, `HAS_PART` and the
rest — a device's location and its duct topology are the same kind of fact.

```csv
source_code,connection_type,target_code
AU-MEL-DEMO-1-101,CONTAINS,VAV-L1-01
AHU-1,FEEDS,VAV-L1-01
```

We store edges in their natural direction; the exporter inverts them, because
DBO declares connections **on the target**, listing sources:

```yaml
VAV-L1-01-guid:
  connections:
    room-101-guid: [CONTAINS]
    ahu-1-guid:    [FEEDS]
```

A device with no `CONTAINS` edge is reported. If your current schema has
`device.floor_id` as a plain column, this graph will not fall out of it
cleanly — that migration is the main cost of adopting DBO, and it is cheaper
now than later.

Code: [`models.Connection`](bms_dbo/models.py),
[`exporter._connections_block`](bms_dbo/exporter.py), `dbo_connection` in
[`schema.sql`](schema.sql).

### 6. Run the validator in CI

[`ci/validate.sh`](ci/validate.sh) — four gates, cheapest first:

```
==> 1/4 unit tests                    299 passed
==> 2/4 ontology pin                  digest matches
==> 3/4 offline mapping validation    0 errors, 1 warning
==> 4/4 DBO instance validator        All entities validated SUCCESSFULLY
```

Gates 1–3 are this repository's own code and run in about a second. Gate 4 runs
the **upstream** `tools/validators/instance_validator`, which stays the
authority — `mapping_validator.py` is a fast inner loop, never a replacement.
The script skips gate 4 loudly if the validator is not installed rather than
passing quietly.

[`bitbucket-pipelines.yml`](bitbucket-pipelines.yml) has a sample pipeline,
including a nightly ontology-drift check.

---

## Proof it works

```console
$ python -m bms_dbo export
Wrote 10 entities to out/building_config.yaml

$ cd ../tools/validators/instance_validator
$ python instance_validator.py -i ../../../_demo_implementation/out/building_config.yaml
[INFO]  Starting config validation.
[INFO]  Validating entity instance definitions.
[WARNING] Entity ... (FCU-1) provides MISSING translation for field
          /discharge_air_temperature_setpoint ...
[INFO]  All entities validated SUCCESSFULLY.
```

The one warning is the intentional `MISSING` field, justified in the CSV.

---

## What the upstream validator taught us

Three things that are not written down in the ontology YAML, found by running
gate 4 against a config that passed every offline check:

**Space codes follow a regex nobody documents.** `AU-MEL-DEMO-L1` is not a
legal floor code; `AU-MEL-DEMO-1` is. Floors must be a number, a garage/ground
level (`G`, `UG`, `M2`), a basement (`B1`, `2B`), a mezzanine (`3M`) or one of
`R/D/LG/FB/S/SBA/SBB`. Rooms are digits and capitals only. The patterns live in
`tools/validators/instance_validator/validate/entity_instance.py`, and are
mirrored in [`naming.py`](bms_dbo/naming.py) so the check happens while the
engineer is naming the space.

**A zone entity needs links or a translation.** The building-config docs say
zones "often do not have links", but `HVAC/ZONE_HVAC` declares optional fields,
and the validator rejects any entity with a field-bearing type and neither
links nor a translation. We dropped the separate zone entities and had each VAV
`FEEDS` its room directly — which `connections.md` explicitly endorses, and
which is one less layer to maintain.

**`MISSING` needs a written justification**, quoted in full above. Hence the
extra column.

## What an independent correctness review found

Before adding the dashboard, a second pass read every module line by line
looking for exactly the kind of drift that accumulates from iterative
editing. It found four real bugs, none caught by the test suite at the time:

* **Duplicate connection rows produced `[CONTAINS, CONTAINS]` in the exported
  config.** `_connections_block` collected connection types into a list, not
  a set. Two identical rows in `connections.csv` — an easy copy-paste
  mistake — survived into the YAML unchanged. Fixed by grouping into sets;
  `mapping_validator` now also warns when a row is genuinely duplicated, so
  the mistake is visible before export rather than only in the output.
* **`#`-comment rows were silently *not* skipped in `connections.csv`.** The
  loader checked for a leading `#` only in a `code` or `device_code` column.
  `connections.csv` has neither — its identifying column is `source_code` —
  so a commented-out connection was parsed as a real one with a source code
  of `"# disabled for now"`. Fixed by checking whichever column comes first,
  which works for every table regardless of its schema.
* **`demo`'s exit code ignored ontology drift.** `cmd_demo` ran
  `ontology-info` for its printed output but only fed `validate`'s result
  into the process exit code. A drifted pin with an otherwise-clean site
  exited `0`. Fixed by combining both — see `cmd_demo` in
  [`cli.py`](bms_dbo/cli.py).
* **A stray `reporting_field` on a `MISSING` mapping was checked
  inconsistently.** On a reporting device it produced a `WARNING`; the
  identical mistake on a virtual device produced nothing at all, because
  `_check_virtual_mapping` returns early for `missing=True`. Fixed at the
  source: `PointMapping.validate()` now treats `reporting_field` as raw data
  a `MISSING` field must not carry, the same way it already treats
  `native_path` and `native_unit` — so both device kinds get exactly one
  finding, from one place.

Two additional issues were purely cosmetic and fixed without ceremony: dead
code in `Ontology.find_type()` (an unreachable branch left over from an
earlier version of the leading-slash fix) and an unused `ModelError`
exception class that nothing raised or imported.

Every fix has a regression test named after the bug it closes, and the
generated config was re-run through the upstream instance validator
afterward — still `All entities validated SUCCESSFULLY`.

## Other traps worth knowing

**YAML turns `ON` and `OFF` into booleans.** DBO uses both as state names, so
`yaml.safe_load` silently drops two states from `states.yaml` and rewrites
every `ON: "true"` in a translation to `True: "true"`. [`DboLoader`](bms_dbo/ontology.py)
keeps `true`/`false` as booleans (needed for `is_abstract: true`) and leaves
everything else a string. The exporter quotes raw `"true"`/`"false"` values on
the way out, and tests check the round trip in both directions.

**`implements: - /PMP` means the global namespace.** A leading slash is an
explicit global reference. Miss it and roughly a hundred types fail to resolve.

**`*_INITIAL` types match everything.** They set `allow_undefined_fields: true`
as a "not modelled yet" marker, so they score perfectly against any point set
and would top every ranking. Excluded from suggestions.

**Virtual devices have no units.** A link carries only `target_field:
source_field`; the unit and state maps live on the reporting entity's
translation. Unit checks must skip virtual entities or they demand data DBO has
nowhere to put. Our own validator got this wrong first — the sample site caught
it.

**Do not derive `value_range` from the ontology.** The envelope in
`telemetry_fields.yaml` is what is *physically plausible* — `0,94389` litres
per second for a VAV. True, useless, and actively misleading given DBO uses
`value_range` to validate writeback requests. Only ever emit the engineer's
device-specific range. We do use the ontology envelope to *check* that range:
a range outside it usually means the unit is wrong.

```console
[WARNING] FCU-9/zone_air_temperature_sensor: value_max 78.0 is above the
          ontology maximum of 48.887 degrees_celsius; check the unit
```

That is a Fahrenheit sensor mapped as celsius — the kind of mistake that stays
invisible until someone reads a trend six months later.

---

## Adapting this to your BMS

**Take:** the table shapes in `schema.sql`, the pinning approach, the offline
checks in `mapping_validator.py`, the four CI gates, and the traps above.

**Replace:** `loader.py`. The four CSVs stand in for four database tables; in
your product that becomes a repository class over your real schema. Nothing
else in `bms_dbo/` knows the data came from CSV.

**Add** (deliberately out of scope here):

- Writing the model back — this demo is one-way, model → config. Round-tripping
  an existing config into your database is a second, larger job, and ABEL
  already does it if you can accept a spreadsheet.
- `UPDATE` mode. Everything here emits `operation: INITIALIZE`. Brownfield
  edits need per-entity `ADD`/`UPDATE`/`DELETE`/`EXPORT` and `etag` handling,
  which the building-config spec covers.
- Telemetry validation, which needs a live Pub/Sub subscription.
- A UI. `suggest_types` and `validate_site` are shaped to sit behind one.

**A note on GUIDs.** `stable_guid()` derives a deterministic UUID4-shaped id
from `site:code` so that regenerating a config gives a reviewable diff instead
of a wall of noise. That is a convenience for this demo. Production onboarding
should use [`tools/guid_generator`](../tools/guid_generator), which is the
supported path.

## Reading

- [Building configuration format](../ontology/docs/building_config.md) — the
  file this demo produces
- [Ontology concepts](../ontology/docs/ontology.md) — subfields, field
  construction, enumeration
- [Model conventions](../ontology/docs/model.md) — general types, abstract
  functional groups
- [Connections](../ontology/docs/connections.md) — all ten relationship types
- [Learning modules](../README.md#learning-modules) — the slide decks
