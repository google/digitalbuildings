"""Tests for the pure HTML rendering behind the local dashboard.

No sockets here -- every function under test is a plain
``(ontology, site, ...) -> str`` call. The handful of tests that need a real
HTTP round trip live in test_webui.py instead.
"""

from __future__ import annotations

from bms_dbo.models import Connection, Device, PointMapping, Site, Space
from bms_dbo.webui_render import (
    children_by_contains,
    e,
    page,
    render_dashboard,
    render_device,
    render_export,
    render_not_found,
    render_ontology,
    render_site_error,
    render_tree,
    render_validate,
)


class TestEscaping:
    def test_escapes_angle_brackets(self):
        assert e("<script>") == "&lt;script&gt;"

    def test_escapes_quotes(self):
        assert '"' not in e('say "hi"')

    def test_passes_through_plain_text(self):
        assert e("VAV-1") == "VAV-1"

    def test_stringifies_non_strings(self):
        assert e(42) == "42"


class TestPage:
    def test_includes_the_title(self):
        assert "My Title" in page("My Title", "", "<p>body</p>")

    def test_includes_the_body(self):
        assert "<p>body</p>" in page("T", "", "<p>body</p>")

    def test_marks_the_active_nav_item(self):
        html_out = page("T", "validate", "body")
        assert 'href="/validate" class="active"' in html_out

    def test_other_nav_items_are_not_active(self):
        html_out = page("T", "validate", "body")
        assert 'href="/export" class="active"' not in html_out

    def test_escapes_the_title(self):
        assert "<script>" not in page("<script>", "", "body")


class TestContainmentTree:
    def test_builds_a_child_map_from_contains_edges_only(self, site):
        children = children_by_contains(site)
        assert children["AU-MEL-DEMO-1-PLANT"] == ["AHU-1", "GW-1"]

    def test_non_contains_edges_are_excluded(self, site):
        children = children_by_contains(site)
        # AHU-1 FEEDS VAV-L1-01/02; that must not appear as a CONTAINS child.
        assert "VAV-L1-01" not in children.get("AHU-1", [])

    def test_render_tree_reaches_every_device(self, site):
        children = children_by_contains(site)
        html_out = render_tree(site, site.building_code, children)
        for device in site.devices:
            assert device.code in html_out

    def test_render_tree_links_devices_but_not_spaces(self, site):
        children = children_by_contains(site)
        html_out = render_tree(site, site.building_code, children)
        assert "/device/AHU-1" in html_out
        assert "/device/AU-MEL-DEMO-1-PLANT" not in html_out

    def test_a_cycle_does_not_infinite_loop(self):
        """A malformed site could declare A CONTAINS B CONTAINS A."""
        site = Site(
            building_code="X",
            spaces=[Space("A", "FACILITIES/ROOM"), Space("B", "FACILITIES/ROOM")],
            connections=[
                Connection("A", "CONTAINS", "B"),
                Connection("B", "CONTAINS", "A"),
            ],
        )
        children = children_by_contains(site)
        # Must return, not hang.
        html_out = render_tree(site, "A", children)
        assert "A" in html_out and "B" in html_out


class TestDashboard:
    def test_shows_the_building_code(self, ontology, site):
        assert site.building_code in render_dashboard(ontology, {}, site)

    def test_lists_every_device(self, ontology, site):
        html_out = render_dashboard(ontology, {}, site)
        assert all(d.code in html_out for d in site.devices)

    def test_shows_the_device_count(self, ontology, site):
        html_out = render_dashboard(ontology, {}, site)
        assert f">{len(site.devices)}<" in html_out

    def test_marks_pin_drift(self, ontology, site):
        html_out = render_dashboard(ontology, {"drifted": True}, site)
        assert "drifted" in html_out

    def test_marks_pin_as_ok_when_not_drifted(self, ontology, site):
        html_out = render_dashboard(ontology, {"drifted": False}, site)
        assert "pin-ok" in html_out

    def test_a_clean_device_gets_the_clean_badge(self, ontology, site):
        html_out = render_dashboard(ontology, {}, site)
        assert "badge-ok\">clean" in html_out

    def test_reporting_vs_virtual_counts_are_correct(self, ontology, site):
        html_out = render_dashboard(ontology, {}, site)
        reporting = sum(1 for d in site.devices if d.is_reporting)
        virtual = sum(1 for d in site.devices if not d.is_reporting)
        assert f">{reporting}<" in html_out and f">{virtual}<" in html_out


class TestDeviceDetail:
    def test_returns_none_for_an_unknown_device(self, ontology, site):
        assert render_device(ontology, site, "NOPE") is None

    def test_shows_the_assigned_type(self, ontology, site):
        html_out = render_device(ontology, site, "AHU-1")
        assert "HVAC/AHU_DFSS_DTC_CHWVM_RTM" in html_out

    def test_the_exact_canonical_match_is_starred(self, ontology, site):
        html_out = render_device(ontology, site, "AHU-1")
        assert "&#9733;" in html_out

    def test_a_gateway_gets_the_nothing_to_infer_message(self, ontology, site):
        html_out = render_device(ontology, site, "GW-1")
        assert "nothing to infer" in html_out

    def test_shows_a_missing_field_with_its_justification(self, ontology, site):
        html_out = render_device(ontology, site, "FCU-1")
        assert "MISSING" in html_out
        assert "Controller exposes no" in html_out

    def test_shows_a_linked_field_for_a_virtual_device(self, ontology, site):
        html_out = render_device(ontology, site, "VAV-L1-01")
        assert "zone_air_temperature_sensor_1" in html_out

    def test_shows_incoming_connections(self, ontology, site):
        html_out = render_device(ontology, site, "VAV-L1-01")
        assert "FEEDS" in html_out and "CONTAINS" in html_out

    def test_an_unknown_dbo_field_is_flagged(self, ontology):
        site = Site(
            building_code="AU-TST-X",
            spaces=[Space("AU-TST-X-1-101", "FACILITIES/ROOM")],
            devices=[Device("D-1", "HVAC/FCU", True, cloud_device_id="1")],
            mappings=[PointMapping("D-1", "not_a_real_field", "points.x")],
            connections=[Connection("AU-TST-X-1-101", "CONTAINS", "D-1")],
        )
        html_out = render_device(ontology, site, "D-1")
        assert "unknown field" in html_out


class TestValidatePage:
    def test_shows_no_errors_when_clean(self, ontology, site):
        html_out = render_validate(ontology, site)
        assert "no errors" in html_out

    def test_shows_the_warning_count(self, ontology, site):
        html_out = render_validate(ontology, site)
        assert "1 warning" in html_out

    def test_renders_a_finding_message(self, ontology, site):
        html_out = render_validate(ontology, site)
        assert "declared MISSING" in html_out


class TestExportPage:
    def test_renders_the_config_when_clean(self, ontology, site):
        html_out = render_export(ontology, site)
        assert "CONFIG_METADATA" in html_out

    def test_offers_a_download_link(self, ontology, site):
        assert "/export/download" in render_export(ontology, site)

    def test_blocks_export_when_there_are_errors(self, ontology, site):
        site.mappings.append(PointMapping("AHU-1", "not_a_real_field", "points.x"))
        html_out = render_export(ontology, site)
        assert "Export blocked" in html_out

    def test_blocked_export_shows_no_yaml(self, ontology, site):
        site.mappings.append(PointMapping("AHU-1", "not_a_real_field", "points.x"))
        html_out = render_export(ontology, site)
        assert "CONFIG_METADATA" not in html_out


class TestOntologyPage:
    def test_shows_the_pinned_digest(self, ontology):
        html_out = render_ontology(ontology, {"pinned_digest": "abc123"})
        assert "abc123" in html_out

    def test_shows_drift_warning(self, ontology):
        html_out = render_ontology(ontology, {"drifted": True})
        assert "has changed" in html_out

    def test_shows_entity_type_count(self, ontology):
        html_out = render_ontology(ontology, {})
        assert str(len(ontology.types)) in html_out


class TestErrorPages:
    def test_not_found_names_the_path(self):
        assert "/nowhere" in render_not_found("/nowhere")

    def test_site_error_shows_the_message(self):
        assert "boom" in render_site_error(ValueError("boom"))
# AI:E87M claude-code 2026-08-27 s:2a846146
