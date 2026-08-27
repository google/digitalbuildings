"""Command line entry point: ``python -m bms_dbo <command>``.

Commands map one-to-one onto the recommendations the README walks through:

    ontology-info     #2  which ontology revision is pinned, and is it current
    suggest-types     #3  rank DBO types from a device's mapped point set
    validate          #1 #4 #5  check every mapping, type and edge
    export            emit the building configuration file
    demo              run all of the above end to end
    serve             the same four things, in a browser -- see webui.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .exporter import build_config, dump_config, write_config
from .loader import load_site
from .mapping_validator import error_count, validate_site
from .models import Site
from .ontology import Ontology, load_pinned_ontology
from .type_matcher import explain_choice, suggest_types

DEMO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITE = DEMO_ROOT / "sample_site"
DEFAULT_PIN = DEMO_ROOT / "ontology_pin.yaml"
DEFAULT_OUT = DEMO_ROOT / "out" / "building_config.yaml"

RULE = "=" * 72


def _heading(text: str) -> None:
    print(f"\n{RULE}\n{text}\n{RULE}")


def cmd_ontology_info(ontology: Ontology, pin: dict, _: Site) -> int:
    """#2 -- prove which ontology this build is speaking."""
    print(f"pinned digest   : {pin.get('pinned_digest') or '(not pinned)'}")
    print(f"actual digest   : {pin.get('actual_digest')}")
    print(f"repo revision   : {pin.get('actual_revision') or '(not a git checkout)'}")
    print(f"resources root  : {ontology.root}")
    print(f"entity types    : {len(ontology.types)}")
    print(f"standard fields : {len(ontology.fields)}")
    print(f"states          : {len(ontology.states)}")
    print(f"unit families   : {len(ontology.units)}")
    if pin.get("drifted"):
        print(
            "\nWARNING: the vendored ontology content has changed since it "
            "was pinned.\n         Re-run mapping validation for every site, "
            "then update ontology_pin.yaml."
        )
        return 1
    return 0


def cmd_suggest_types(ontology: Ontology, _: dict, site: Site) -> int:
    """#3 -- infer the entity type from the points, do not ask for it."""
    for device in site.devices:
        declared = site.declared_fields(device.code)
        if not declared:
            continue
        print(f"\n{device.code}  ({len(declared)} field(s) declared)")
        print(f"  assigned : {device.entity_type}")
        assigned = ontology.find_type(device.entity_type)
        if assigned is not None and assigned.allow_undefined_fields:
            # A gateway is not a modelled device. Its enumerated fields belong
            # to the entities that link to them, so ranking types for it would
            # just re-suggest whatever is downstream.
            print(
                "             -> accepts undefined fields; nothing to infer "
                "(the linked entities carry the model)"
            )
            continue
        general = device.general_type if device.namespace == "HVAC" else None
        candidates = suggest_types(
            ontology,
            declared,
            namespace=device.namespace,
            general_type=general,
            limit=3,
        )
        scored = explain_choice(ontology, device.entity_type, declared)
        print(f"             -> {scored.summary()}")
        if not candidates:
            print("  suggested: (no type covers this point set)")
            continue
        print("  suggested:")
        for rank, candidate in enumerate(candidates, start=1):
            marker = "*" if candidate.qualified_name == device.entity_type else " "
            print(
                f"   {marker}{rank}. {candidate.qualified_name:<38} "
                f"{candidate.summary()}"
            )
    return 0


def cmd_validate(ontology: Ontology, _: dict, site: Site) -> int:
    """#1 #4 #5 -- every mapping, type and edge checked offline."""
    findings = validate_site(ontology, site)
    if not findings:
        print("No findings. Site is internally consistent.")
        return 0
    for finding in findings:
        print(f"  {finding.format()}")
    errors = error_count(findings)
    warnings = len(findings) - errors
    print(f"\n{errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


def cmd_export(ontology: Ontology, _: dict, site: Site, out: Path) -> int:
    config = build_config(ontology, site)
    findings = validate_site(ontology, site)
    if error_count(findings):
        print("Refusing to export: fix the errors reported by `validate` first.")
        return 1
    written = write_config(config, out)
    entities = len(config) - 1  # CONFIG_METADATA is not an entity
    print(f"Wrote {entities} entities to {written}")
    return 0


def cmd_demo(ontology: Ontology, pin: dict, site: Site, out: Path) -> int:
    _heading("1. Which ontology are we speaking?  (recommendation #2)")
    ontology_status = cmd_ontology_info(ontology, pin, site)

    _heading("2. Type suggested from the mapped points  (recommendation #3)")
    cmd_suggest_types(ontology, pin, site)

    _heading("3. Mapping, type and location checks  (#1, #4, #5)")
    validate_status = cmd_validate(ontology, pin, site)
    # Either section failing should fail the whole walkthrough -- a caller
    # checking only this exit code must see ontology drift, not just mapping
    # errors.
    status = max(ontology_status, validate_status)

    _heading("4. Exported building configuration")
    config = build_config(ontology, site)
    text = dump_config(config)
    preview = text.splitlines()
    for line in preview[:45]:
        print(line)
    if len(preview) > 45:
        print(f"... ({len(preview) - 45} more lines)")
    write_config(config, out)
    print(f"\nFull config written to {out}")
    return status


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bms_dbo",
        description="Reference implementation of DBO support inside a BMS.",
    )
    parser.add_argument(
        "command",
        choices=[
            "ontology-info",
            "suggest-types",
            "validate",
            "export",
            "demo",
            "serve",
        ],
    )
    parser.add_argument("--site", type=Path, default=DEFAULT_SITE)
    parser.add_argument("--pin", type=Path, default=DEFAULT_PIN)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--host", default="127.0.0.1", help="serve: address to bind (default 127.0.0.1)"
    )
    parser.add_argument(
        "--port", type=int, default=8765, help="serve: port to bind (default 8765)"
    )
    parser.add_argument(
        "--no-browser",
        dest="open_browser",
        action="store_false",
        help="serve: do not open a browser tab automatically",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    ontology, pin = load_pinned_ontology(args.pin)

    if args.command == "serve":
        from .webui import serve as run_server

        run_server(
            ontology,
            pin,
            args.site,
            host=args.host,
            port=args.port,
            open_tab=args.open_browser,
        )
        return 0

    site = load_site(args.site)

    if args.command == "ontology-info":
        return cmd_ontology_info(ontology, pin, site)
    if args.command == "suggest-types":
        return cmd_suggest_types(ontology, pin, site)
    if args.command == "validate":
        return cmd_validate(ontology, pin, site)
    if args.command == "export":
        return cmd_export(ontology, pin, site, args.out)
    return cmd_demo(ontology, pin, site, args.out)


if __name__ == "__main__":
    sys.exit(main())
# AI:E87M claude-code 2026-08-27 s:2a846146
