# Digital Buildings Ontology Configuration

The Digital Buildings ontology uses [YAML](http://yaml.org) syntax to define its
models. The format allows users to specify subfields, fields, entity types,
states, units and connections in multiple namespaces. Files written in the
format can be strictly validated for consistency and backwards compatibility
with earlier versions.

*   For an explanation of the existing abstract model see [model](model.md)
*   For a conceptual explanation of the ontology see [ontology](ontology.md)

- [Digital Buildings Ontology Configuration](#digital-buildings-ontology-configuration)
  * [Namespaces and File Structure](#namespaces-and-file-structure)
  * [Namespace-aware Components](#namespace-aware-components)
  * [Namespace Agnostic Components](#namespace-agnostic-components)
  * [Namespace Elevation](#namespace-elevation)
  * [Configuration Syntax](#configuration-syntax)
    + [Subfields](#subfields)
    + [Fields and Multi-state groups](#fields-and-multi-state-groups)
      - [Elevating Fields](#elevating-fields)
    + [States](#states)
    + [EntityTypes](#entitytypes)
    + [Connections (coming soon)](#connections--coming-soon-)
    + [Units](#units)
  * [Validation](#validation)
  * [Notes](#notes)

## Namespaces and File Structure

Each namespace in the ontology has folders with reserved names for each type
component: `fields`, `subfields`, `entity_types` and `states`. The global
namespace has two additional folders `units` and `connections`(coming soon), as
well as folders for each of the child namespaces.

Child namespaces are defined by adding subfolders to the global namespace with
the name of the child namespace. Child namespace names that overlap with
reserved folder names are, obviously, not allowed. Only one level of child
namespaces is allowed.

File names and subfolder hierarchy below the reserved folder names are ignored
for the purposes of constructing the ontology. All files in all
folders under a reserved folder will be read and consolidated into the model as
if they had been defined in a single file.

## Namespace-aware Components

Fields, EntityTypes and MultiStates all carry explicit namespaces. That is, if a
user defines any of these components in a namespace and it cannot be
[elevated](#elevating-names) to the global namespace, it carries that qualifier
everywhere in the system. Ex: `HVAC/zone_temperature_sensor`.

Because of namespace elevation, states in field files and fields in entity type
files can always be written with the namespace omitted. The only case where a
namespace is required is when a user is referring to a non-elevated field in
another namespace. This imposes a few constraints on components, which will be
discussed later.

## Namespace Agnostic Components

**Subfields**: Unlike other components, are Subfields are not namespace aware.
As a result, they are always used verbatim and should be defined in the global
namespace whenever possible. Subfields defined in a non-global namespace are
only available for use in that namespace and conflicting subfields in the local
namespace will override the definition of the globally defined versions for any
fields defined in that namespace.

**Units and Connections**: Units and connections are always defined globally.

## Namespace Elevation

[Namespace elevation](ontology.md#namespace-elevation) is the concept of pushing
definitions from child namespaces to the global namespace when doing so is
guaranteed safe. Field definitions are subject to namespace elevation.
Functionally this means that a field, regardless of where it is defined, will be
considered global if it only uses subfields in the global namespace. From a
syntax perspective, an elevated field can always be referenced without being
fully qualified.

## Configuration Syntax

### Subfields

Subfields are described in a folder with the name `subfields`. Subfields are
primarily defined at the top level of the BOS ontology, but top level
definitions for all except measurement subfields may be overridden in local
namespaces (though this is discouraged).

In order to minimize repetitive text, subfields are grouped by type, then
defined as key:value mappings consisting of the subfield name and a definition.
Example:

```
aggregation:
  max: The largest value ...
  Min: The smallest value ...
component:
  Fan: ...
  Pump: ...
descriptor:
  ...
measurement:
  ...
measurement_descriptor:
  ...
point_type:
  setpoint: A value the system controls to on a particular dimension
  ...
```

The value for the key is simply a free-text description of the subfield's
meaning.

The validation enforces that:

*   All subfields begin with a lowercase alpha character
*   No subfield names are duplicated within the namespace
*   Measurement subfields are defined only in the global namespace
*   All Measurement subfields have mappings in the [units](#units) config

### Fields and Multi-state groups

Fields are described in a folder with the name `fields`. They can be configured
in the global namespace or in individual namespaces. There is no particular
preference for definition at the top level or in namespaces (since fields are
elevated whenever possible). The parser should automatically sort fields into
the global or local namespace depending on whether or not they can be elevated.

Fields are added in fully constructed form using the `"literals"` tag[^5].

```
literals:
- zone_air_temperature_sensor
- zone_air_temperature_setpoint
- zone_air_temperature_mode:
  - AUTO
  - OCCUPIED
  - UNOCCUPIED
```

Users may also define the values for any multi-states (any field with a status
or command point type) inline as a nested array. Each state is considered a
reference to a state value in the global namespace unless a state with the same
name is defined in the local namespace, in which case the definition is assumed
to use the local version.

Use of locally defined states across namespaces is not currently supported as it
would require support for aliasing of unqualified state names[^2].

See [Ontology Fields](ontology.md#fields) for more detail on field construction
rules.

The validation enforces that:

*   fields only use defined subfields
*   only one instance of a subfield set exists in each namespace
*   fields follow construction rules
*   only defined states are assigned to fields
*   each state is only defined once in a multi-state group for a field

#### Elevating Fields

When building the ontology, any fields using all globally defined subcomponents
are created in the global namespace. Field validation for duplicates is done in
the namespace the field arrives in after elevation.

### States

States are described in a folder with the name `states`. States may be defined
globally or in local namespaces, with a preference for global definitions for
any state that is likely to be reusable.

**Unlike fields, multistates are always namespaced based on the subfolder they
reside in.** They are listed in a file called "states". Configuration is a
simple key:value pairing of the name and the definition:

```
ON: This thing is running
OFF: This thing is not running
```

Validation enforces:

*   Keys are unique per namespace.
*   Keys begin with a alpha-character
*   A test description is provided

### EntityTypes

Entity types are described in a folder with the name `entity_types`. Entity
types are the most often namespaced component. Each Entity Type specifies the
fields and inherited types that compose it. Entity Types are namespaced like
fields and can used both locally and globally namespaced fields and types in
their construction.

A typical construction looks like this:

```
variable_air_volume_terminal:
  description: this is a really common HVAC device
  is_abstract: false // note: this defaults to false if unspecified
  is_canonical: false // defaults to false.  See this doc for detail
  implements:
  - some_parent_type
  - another_parent_type
  uses:
  - discharge_air_flowrate_setpoint
  - discharge_air_flowrate_sensor
  opt_uses:
  - discharge_air_temperature_sensor
  connections:  # NB:  Connection constraints are not yet implemented
  - air_handler_type: FEEDS
  - chilled_water_plant_type: FEEDS

```

*   `description`: A plain-text explanation of what this type represents. The
    definition is particularly important because types have inherent meaning
    independent of the fields they contain.
*   `is_abstract`: set true if this type cannot be assigned directly to an
    entity
*   `is_canonical`: set true if this is a preferred type in your model
*   `implements`: lists parents that this type will inherit fields and
    relationship constraints from
*   `uses`: required fields for this type
*   `opt_uses`: optional fields for this type
*   `connections`: required connections this type must be a target of.
    Specification is `<source type>:<connection type>`

When specifying an entity, the user can add fields or other entities either in
the local namespace or the global one verbatim, as the parser should be able to
explicitly differentiate between whether or not the user's intent was to specify
a local or global field or entity[^4]. Entries from other local namespaces are
prefixed with `"<namespace>/"`.

Validation enforces:

*   there are no duplicate fields defined directly in `uses` or `opt_uses`
*   all assigned fields, relationships and referenced types exists
*   all type names are unique per-namespace
*   types have text descriptions (warning)

### Connections (coming soon)

Connections are described in a folder with the name `connections`. Connections
can **only** be described in the global namespace, and the set of connections is
intended to grow infrequently.

Connections are defined by name with an associated description[^6]:

```
FEEDS:
  description: Source sends physical media (air, water, etc.) to Target
CONTAINS:
  description: Source physically contains target
```

Validation enforces:

*   All connections are unique
*   All connections have definitions provided

### Units

Units are described in a folder with the name `units`. They are **only** defined
in the global namespace and are grouped by measurement subfield. For example:

```
concentration:
- parts_per_million: STANDARD
current:
- amperes: STANDARD
- milliamperes
energy:
- joules: STANDARD
- kilowatt_hours
```

Under each subfield name, the configuration defines a list of dimensional units
of a single
[Quantity Kind](qudt.org),
One of the listed units must be listed as the `STANDARD` unit for the type. All
of the `STANDARD` units for all subfields must belong to the same unit family,
such as standard SI units.

Validation enforces:

*   Each subfield only has units defined for it one time
*   Each dimensional unit is defined only once in the file
*   Exactly one `STANDARD` designation is made per subfield

## Validation

The Digital Buildings ontology contains a configuration validator that enforces
all the constraints outlined above.

The validator source code can be found [here](TODO:ADD PATH).

The Validator is Python based, it takes the following arguments:

*   original: a path pointing to the original files of the ontology
*   changed (optional): a path pointing to the changed files of the ontology.

The validator can be run as following: `python3 validator.py
--original=Users/foo/ontology/`

## Notes

[^2]: The reason for this requirement is so that compiled code for the ontology
    have clean enumerations. \
[^3]: The "literals" list would also be in its own document, if used. \
[^4]: An unstated assumption here is that the local version of a field is
    assumed to be used when a conflict exists between the local and global
    namespace. A user could explicitly specify a global namespace to override
    this with a leading "/'". \
[^5]: A construction syntax was originally envisioned to help related subfield
    permutations to auto-generate, but we found that in practice the number of
    fields was small enough that it was never implemented. \
[^6]: longer form with `description` added as a separate key anticipates
    additional configuration functionality for fields \
