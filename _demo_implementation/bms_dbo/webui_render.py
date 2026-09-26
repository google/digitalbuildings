"""Pure HTML rendering for the local dashboard.

Every function here is ``(ontology, site, ...) -> HTML string`` and nothing
else -- no sockets, no file writes, no global state. That is what lets
``tests/test_webui_render.py`` cover this module with plain function calls
instead of spinning up a server. The HTTP layer that calls these lives in
``webui.py``.
"""

from __future__ import annotations

import html

from .exporter import build_config, dump_config
from .mapping_validator import Finding, Severity, error_count, validate_site
from .models import Device, Site
from .ontology import Ontology
from .type_matcher import TypeCandidate, explain_choice, suggest_types

# --------------------------------------------------------------------- style

CSS = """
:root {
  --bg: #f7f7f5; --panel: #ffffff; --border: #e2e2df; --text: #1d1d1b;
  --muted: #6b6b66; --accent: #2f6f4f; --accent-bg: #e8f3ec;
  --error: #b3261e; --error-bg: #fbe9e7; --warn: #8a5a00; --warn-bg: #fdf2d9;
  --code-bg: #f1f1ee; --link: #1a5276;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1c1c1a; --panel: #262624; --border: #3a3a37; --text: #ececea;
    --muted: #a3a39c; --accent: #6fbf94; --accent-bg: #223229;
    --error: #ff8a80; --error-bg: #3a2222; --warn: #ffca6b; --warn-bg: #3a3120;
    --code-bg: #1f1f1d; --link: #7fb3d5;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
nav {
  display: flex; gap: 4px; align-items: center; padding: 10px 20px;
  background: var(--panel); border-bottom: 1px solid var(--border);
}
nav b { margin-right: 16px; }
nav a {
  color: var(--muted); text-decoration: none; padding: 6px 12px;
  border-radius: 6px; font-size: 14px;
}
nav a:hover { background: var(--code-bg); }
nav a.active { background: var(--accent-bg); color: var(--accent); font-weight: 600; }
main { max-width: 980px; margin: 0 auto; padding: 24px 20px 60px; }
h1 { font-size: 22px; margin: 0 0 4px; }
h2 { font-size: 16px; margin: 28px 0 10px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.subtitle { color: var(--muted); margin: 0 0 20px; }
.cards { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 8px; }
.card {
  background: var(--panel); border: 1px solid var(--border); border-radius: 10px;
  padding: 14px 18px; min-width: 130px;
}
.card .n { font-size: 24px; font-weight: 700; }
.card .l { color: var(--muted); font-size: 13px; }
table { width: 100%; border-collapse: collapse; background: var(--panel);
  border: 1px solid var(--border); border-radius: 8px; overflow: hidden; }
th, td { text-align: left; padding: 8px 12px; border-bottom: 1px solid var(--border); font-size: 14px; }
th { color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; }
tr:last-child td { border-bottom: none; }
tr:hover td { background: var(--code-bg); }
a { color: var(--link); }
code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
code { background: var(--code-bg); padding: 1px 5px; border-radius: 4px; font-size: 13px; }
pre { background: var(--code-bg); border: 1px solid var(--border); border-radius: 8px;
  padding: 14px; overflow-x: auto; font-size: 13px; line-height: 1.5; }
.badge { display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 12px; font-weight: 600; }
.badge-ok { background: var(--accent-bg); color: var(--accent); }
.badge-error { background: var(--error-bg); color: var(--error); }
.badge-warn { background: var(--warn-bg); color: var(--warn); }
.badge-muted { background: var(--code-bg); color: var(--muted); }
.row-error td:first-child { border-left: 3px solid var(--error); }
.row-warn td:first-child { border-left: 3px solid var(--warn); }
.tree { list-style: none; padding-left: 18px; margin: 4px 0; }
.tree > li { margin: 2px 0; }
.tree-root { padding-left: 0; }
.tree .type { color: var(--muted); font-size: 12px; }
.empty { color: var(--muted); padding: 20px; text-align: center; }
.pin-ok { color: var(--accent); }
.pin-bad { color: var(--error); }
.err-box { background: var(--error-bg); color: var(--error); border-radius: 8px;
  padding: 14px 18px; margin: 16px 0; }
footer { color: var(--muted); font-size: 12px; text-align: center; padding: 30px 0 10px; }
"""

NAV_ITEMS = [
    ("", "Dashboard"),
    ("validate", "Validate"),
    ("export", "Export"),
    ("ontology", "Ontology"),
]


def e(value: object) -> str:
    """Escape text for HTML. Named short because it is used constantly."""
    return html.escape(str(value), quote=True)


def page(title: str, active: str, body: str) -> str:
    """Wrap a body fragment in the page shell -- nav, CSS, footer."""
    nav_links = "".join(
        f'<a href="/{href}" class="{"active" if href == active else ""}">{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · DBO demo</title>
<style>{CSS}</style>
</head><body>
<nav><b>DBO / BMS demo</b>{nav_links}</nav>
<main>{body}</main>
<footer>Reference implementation, not the DBO project itself &middot;
reads sample_site/ fresh on every request</footer>
</body></html>"""


def _severity_badge(severity: Severity) -> str:
    cls = "badge-error" if severity is Severity.ERROR else "badge-warn"
    return f'<span class="badge {cls}">{severity.value}</span>'


def _findings_table(findings: list[Finding]) -> str:
    if not findings:
        return '<p class="empty">No findings. Site is internally consistent.</p>'
    rows = []
    for finding in findings:
        row_cls = "row-error" if finding.severity is Severity.ERROR else "row-warn"
        where = (
            f"{e(finding.entity)} / <code>{e(finding.field_name)}</code>"
            if finding.field_name
            else e(finding.entity)
        )
        rows.append(
            f"<tr class='{row_cls}'><td>{_severity_badge(finding.severity)}</td>"
            f"<td>{where}</td><td>{e(finding.message)}</td></tr>"
        )
    return (
        "<table><thead><tr><th>Severity</th><th>Entity / field</th>"
        f"<th>Message</th></tr></thead><tbody>{''.join(rows)}</tbody></table>"
    )


def _device_badge(device: Device) -> str:
    return (
        '<span class="badge badge-ok">reporting</span>'
        if device.is_reporting
        else '<span class="badge badge-muted">virtual</span>'
    )


# ------------------------------------------------------------ containment tree


def children_by_contains(site: Site) -> dict[str, list[str]]:
    children: dict[str, list[str]] = {}
    for connection in site.connections:
        if connection.connection_type == "CONTAINS":
            children.setdefault(connection.source_code, []).append(
                connection.target_code
            )
    return children


def _entity_type_of(site: Site, code: str) -> str:
    """The entity type string for a code that may be any entity kind."""
    if code == site.building_code:
        return "FACILITIES/BUILDING"
    space = site.space(code)
    if space is not None:
        return space.entity_type
    device = site.device(code)
    if device is not None:
        return device.entity_type
    return "?"


def render_tree(site: Site, code: str, children: dict[str, list[str]]) -> str:
    """Recursive ``CONTAINS`` tree starting at *code*. Cycle-safe."""

    def node(current: str, seen: frozenset[str]) -> str:
        entity_type = _entity_type_of(site, current)
        device = site.device(current)
        label = (
            f'<a href="/device/{e(current)}">{e(current)}</a>'
            if device is not None
            else e(current)
        )
        line = f"{label} <span class='type'>{e(entity_type)}</span>"
        kids = [c for c in children.get(current, []) if c not in seen]
        if not kids:
            return f"<li>{line}</li>"
        inner = "".join(node(kid, seen | {kid}) for kid in kids)
        return f"<li>{line}<ul class='tree'>{inner}</ul></li>"

    return f"<ul class='tree tree-root'>{node(code, frozenset({code}))}</ul>"


# ---------------------------------------------------------------- dashboard


def _device_status_badge(device_findings: list[Finding]) -> str:
    if any(f.severity is Severity.ERROR for f in device_findings):
        return '<span class="badge badge-error">issues</span>'
    if device_findings:
        return '<span class="badge badge-warn">warnings</span>'
    return '<span class="badge badge-ok">clean</span>'


def render_dashboard(ontology: Ontology, pin: dict, site: Site) -> str:
    findings = validate_site(ontology, site)
    errors = error_count(findings)
    warnings = len(findings) - errors
    children = children_by_contains(site)

    device_rows = [
        "<tr><td><a href='/device/{code}'>{code}</a></td>"
        "<td><code>{etype}</code></td><td>{kind}</td>"
        "<td>{n} field(s)</td><td>{status}</td></tr>".format(
            code=e(device.code),
            etype=e(device.entity_type),
            kind=_device_badge(device),
            n=len(site.declared_fields(device.code)),
            status=_device_status_badge(
                [f for f in findings if f.entity == device.code]
            ),
        )
        for device in sorted(site.devices, key=lambda d: d.code)
    ]

    pin_status = (
        '<span class="pin-bad">drifted</span>'
        if pin.get("drifted")
        else '<span class="pin-ok">pinned</span>'
    )

    return f"""
<h1>{e(site.building_code)}</h1>
<p class="subtitle">{len(site.spaces)} space(s) &middot;
{len(site.devices)} device(s) &middot; ontology {pin_status}</p>

<div class="cards">
  <div class="card"><div class="n">{len(site.devices)}</div><div class="l">Devices</div></div>
  <div class="card"><div class="n">{sum(1 for d in site.devices if d.is_reporting)}</div>
      <div class="l">Reporting</div></div>
  <div class="card"><div class="n">{sum(1 for d in site.devices if not d.is_reporting)}</div>
      <div class="l">Virtual</div></div>
  <div class="card"><div class="n" style="color:var(--error)">{errors}</div>
      <div class="l">Errors</div></div>
  <div class="card"><div class="n" style="color:var(--warn)">{warnings}</div>
      <div class="l">Warnings</div></div>
</div>

<h2>Building layout</h2>
{render_tree(site, site.building_code, children)}

<h2>Devices</h2>
<table><thead><tr><th>Code</th><th>Entity type</th><th>Kind</th>
<th>Points declared</th><th>Status</th></tr></thead>
<tbody>{"".join(device_rows) or "<tr><td colspan=5 class='empty'>No devices.</td></tr>"}</tbody></table>
"""


# --------------------------------------------------------------- device page


def _candidate_row(candidate: TypeCandidate, assigned_type: str) -> str:
    marker = " &#9733;" if candidate.qualified_name == assigned_type else ""
    return (
        f"<tr><td><code>{e(candidate.qualified_name)}</code>{marker}</td>"
        f"<td>{e(candidate.summary())}</td></tr>"
    )


def _mapping_row(ontology: Ontology, mapping) -> str:
    if mapping.missing:
        value = "<span class='badge badge-warn'>MISSING</span>"
        detail = e(mapping.missing_justification or "(no justification)")
    elif mapping.reporting_field:
        value = f"&#8592; <code>{e(mapping.reporting_field)}</code>"
        detail = "linked field"
    else:
        unit = (
            f" <span class='type'>{e(mapping.dbo_unit)}</span>"
            if mapping.dbo_unit
            else ""
        )
        states = (
            ", ".join(f"{k}={v}" for k, v in sorted(mapping.native_states.items()))
            if mapping.native_states
            else ""
        )
        value = f"<code>{e(mapping.native_path)}</code>{unit}"
        detail = e(states)
    definition = ontology.get_field(mapping.dbo_field)
    unknown = "" if definition else " <span class='badge badge-error'>unknown field</span>"
    return (
        f"<tr><td><code>{e(mapping.dbo_field)}</code>{unknown}</td>"
        f"<td>{value}</td><td>{detail}</td></tr>"
    )


def _type_candidates_html(ontology: Ontology, device: Device, declared: set) -> str:
    try:
        entity = ontology.find_type(device.entity_type)
    except Exception:  # noqa: BLE001 - fall through to "not applicable"
        entity = None
    if entity is not None and entity.allow_undefined_fields:
        return (
            "<p class='empty'>This type accepts undefined fields (a gateway "
            "or passthrough) &mdash; nothing to infer. The entities that link "
            "to it carry the model.</p>"
        )
    if not declared:
        return "<p class='empty'>No points mapped yet.</p>"
    general = device.general_type if device.namespace == "HVAC" else None
    candidates = suggest_types(
        ontology, declared, namespace=device.namespace,
        general_type=general, limit=5,
    )
    rows = "".join(_candidate_row(c, device.entity_type) for c in candidates)
    return (
        "<table><thead><tr><th>Candidate type</th><th>Fit</th></tr></thead>"
        f"<tbody>{rows or '<tr><td colspan=2>No complete match.</td></tr>'}</tbody></table>"
    )


def render_device(ontology: Ontology, site: Site, code: str) -> str | None:
    device = site.device(code)
    if device is None:
        return None

    declared = site.declared_fields(code)
    all_findings = validate_site(ontology, site)
    device_findings = [f for f in all_findings if f.entity == code]

    candidates_html = _type_candidates_html(ontology, device, declared)
    assigned = ontology.find_type(device.entity_type)
    if declared and not (assigned is not None and assigned.allow_undefined_fields):
        scored = explain_choice(ontology, device.entity_type, declared)
        assigned_summary = (
            f"<p><strong>Assigned type:</strong> <code>{e(device.entity_type)}</code> "
            f"&mdash; {e(scored.summary())}</p>"
        )
    else:
        assigned_summary = (
            f"<p><strong>Assigned type:</strong> "
            f"<code>{e(device.entity_type)}</code></p>"
        )

    mapping_rows = "".join(
        _mapping_row(ontology, m)
        for m in sorted(site.mappings_for(code), key=lambda m: m.dbo_field)
    )

    location = "".join(
        f"<li>{e(c.connection_type)} from <code>{e(c.source_code)}</code></li>"
        for c in site.connections_into(code)
    )

    origin = (
        f"cloud_device_id: <code>{e(device.cloud_device_id)}</code>"
        if device.is_reporting
        else f"linked from <code>{e(device.reporting_device_code)}</code>"
    )

    return f"""
<p><a href="/">&larr; Dashboard</a></p>
<h1>{e(code)}</h1>
<p class="subtitle">{_device_badge(device)} {origin}</p>

{assigned_summary}

<h2>Suggested types (recommendation #3)</h2>
{candidates_html}

<h2>Point mappings ({len(declared)})</h2>
<table><thead><tr><th>DBO field</th><th>Source</th><th>Detail</th></tr></thead>
<tbody>{mapping_rows or "<tr><td colspan=3 class='empty'>No points mapped.</td></tr>"}</tbody></table>

<h2>Incoming connections</h2>
<ul>{location or "<li class='empty'>No connections point at this device.</li>"}</ul>

<h2>Validation findings for this device</h2>
{_findings_table(device_findings)}
"""


# -------------------------------------------------------------- other pages


def render_validate(ontology: Ontology, site: Site) -> str:
    findings = validate_site(ontology, site)
    errors = error_count(findings)
    warnings = len(findings) - errors
    status_badge = (
        f'<span class="badge badge-error">{errors} error(s)</span>'
        if errors
        else '<span class="badge badge-ok">no errors</span>'
    )
    return f"""
<h1>Validation</h1>
<p class="subtitle">{status_badge}
<span class="badge badge-warn">{warnings} warning(s)</span></p>
<p>Runs the offline checks in <code>mapping_validator.py</code>: field names,
units, states, required fields, MISSING justification, location edges and
FACILITIES naming. The upstream DBO instance validator remains the final
authority &mdash; see <code>ci/validate.sh</code>.</p>
{_findings_table(findings)}
"""


def render_export(ontology: Ontology, site: Site) -> str:
    findings = validate_site(ontology, site)
    errors = error_count(findings)
    if errors:
        return f"""
<h1>Export</h1>
<div class="err-box"><strong>Export blocked.</strong> {errors} error(s) must
be fixed first &mdash; see <a href="/validate">Validate</a>.</div>
"""
    config = build_config(ontology, site)
    text = dump_config(config)
    entity_count = len(config) - 1
    return f"""
<h1>Export</h1>
<p class="subtitle">{entity_count} entities &middot; ready for
<code>tools/validators/instance_validator</code></p>
<p><a href="/export/download">Download building_config.yaml</a></p>
<pre>{e(text)}</pre>
"""


def render_ontology(ontology: Ontology, pin: dict) -> str:
    pin_row = (
        '<div class="err-box">The vendored ontology content has changed '
        "since it was pinned. Re-run validation for every site, then update "
        "ontology_pin.yaml.</div>"
        if pin.get("drifted")
        else '<p><span class="badge badge-ok">digest matches pin</span></p>'
    )
    return f"""
<h1>Ontology</h1>
{pin_row}
<table>
<tr><th>Pinned digest</th><td><code>{e(pin.get('pinned_digest') or '(not pinned)')}</code></td></tr>
<tr><th>Actual digest</th><td><code>{e(pin.get('actual_digest'))}</code></td></tr>
<tr><th>Repo revision</th><td><code>{e(pin.get('actual_revision') or 'n/a')}</code></td></tr>
<tr><th>Resources root</th><td><code>{e(ontology.root)}</code></td></tr>
<tr><th>Entity types</th><td>{len(ontology.types)}</td></tr>
<tr><th>Standard fields</th><td>{len(ontology.fields)}</td></tr>
<tr><th>States</th><td>{len(ontology.states)}</td></tr>
<tr><th>Unit families</th><td>{len(ontology.units)}</td></tr>
</table>
"""


def render_not_found(path: str) -> str:
    return (
        f"<h1>Not found</h1><p><code>{e(path)}</code> has no page here. "
        f"<a href='/'>Back to the dashboard</a>.</p>"
    )


def render_site_error(error: Exception) -> str:
    return (
        "<h1>Site failed to load</h1>"
        f"<div class='err-box'>{e(error)}</div>"
        "<p>Fix the CSV and refresh this page &mdash; the site is re-read on "
        "every request.</p>"
    )
# AI:E87M claude-code 2026-08-27 s:2a846146
