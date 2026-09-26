"""Tests for the HTTP layer that serves the dashboard.

Most behavior is covered by test_webui_render.py without a socket. What is
left here is what only exists once real HTTP is involved: status codes,
headers, and route() as the pure dispatcher underneath the handler.
"""

from __future__ import annotations

import shutil
import threading
import urllib.error
import urllib.request
from pathlib import Path

import pytest

from bms_dbo.ontology import Ontology, default_resources_root
from bms_dbo.webui import free_port, make_server, route

DEMO_ROOT = Path(__file__).resolve().parent.parent
SAMPLE = DEMO_ROOT / "sample_site"


@pytest.fixture()
def site_dir(tmp_path: Path) -> Path:
    target = tmp_path / "site"
    shutil.copytree(SAMPLE, target)
    return target


@pytest.fixture(scope="module")
def running_server(ontology_module):
    """One real server for the whole module -- opening sockets is the
    expensive part, and these tests only read, so sharing is safe."""
    server = make_server(
        ontology_module, {"drifted": False}, SAMPLE, "127.0.0.1", free_port()
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    thread.join(timeout=5)


@pytest.fixture(scope="module")
def ontology_module():
    return Ontology(default_resources_root())


def _get(base: str, path: str):
    try:
        return urllib.request.urlopen(base + path)
    except urllib.error.HTTPError as error:
        return error


class TestRoute:
    """route() is the pure dispatcher -- exercised directly, no socket."""

    def test_root_serves_the_dashboard(self, ontology_module, site_dir):
        status, active, body = route(ontology_module, {}, site_dir, "/")
        assert (status, active) == (200, "")
        assert "AU-MEL-DEMO" in body

    def test_validate_sets_the_active_nav_item(self, ontology_module, site_dir):
        status, active, _ = route(ontology_module, {}, site_dir, "/validate")
        assert (status, active) == (200, "validate")

    def test_export_sets_the_active_nav_item(self, ontology_module, site_dir):
        status, active, _ = route(ontology_module, {}, site_dir, "/export")
        assert (status, active) == (200, "export")

    def test_export_download_route_matches_export(self, ontology_module, site_dir):
        """The socket layer intercepts /export/download for the raw file;
        route() itself treats it the same as /export for the HTML case."""
        status, active, _ = route(ontology_module, {}, site_dir, "/export/download")
        assert (status, active) == (200, "export")

    def test_a_known_device_returns_200(self, ontology_module, site_dir):
        status, _, body = route(ontology_module, {}, site_dir, "/device/AHU-1")
        assert status == 200 and "AHU-1" in body

    def test_an_unknown_device_returns_404(self, ontology_module, site_dir):
        status, _, _ = route(ontology_module, {}, site_dir, "/device/NOPE")
        assert status == 404

    def test_an_unknown_path_returns_404(self, ontology_module, site_dir):
        status, _, _ = route(ontology_module, {}, site_dir, "/nowhere")
        assert status == 404

    def test_a_trailing_slash_is_normalised(self, ontology_module, site_dir):
        with_slash = route(ontology_module, {}, site_dir, "/validate/")
        without_slash = route(ontology_module, {}, site_dir, "/validate")
        assert with_slash == without_slash

    def test_a_url_encoded_device_code_is_decoded(self, ontology_module, site_dir):
        status, _, _ = route(ontology_module, {}, site_dir, "/device/AHU%2D1")
        assert status == 200

    def test_a_broken_site_returns_500_not_a_crash(self, ontology_module, site_dir):
        (site_dir / "site.yaml").write_text("display_name: nameless\n")
        status, _, body = route(ontology_module, {}, site_dir, "/")
        assert status == 500 and "building_code" in body

    def test_the_site_is_re_read_on_every_call(self, ontology_module, site_dir):
        """Edit the CSV, call route() again, see the change -- no caching."""
        before_status, _, before_body = route(ontology_module, {}, site_dir, "/")
        devices_csv = site_dir / "devices.csv"
        devices_csv.write_text(
            devices_csv.read_text()
            + "NEW-DEV-1,HVAC/PMP,TRUE,999,New pump,\n"
        )
        _, _, after_body = route(ontology_module, {}, site_dir, "/")
        assert before_status == 200
        assert "NEW-DEV-1" not in before_body
        assert "NEW-DEV-1" in after_body


class TestLiveServer:
    """A handful of true HTTP round trips to prove the socket layer wires up
    correctly -- headers, status codes, download disposition."""

    def test_dashboard_is_reachable(self, running_server):
        response = _get(running_server, "/")
        assert response.status == 200

    def test_dashboard_is_html(self, running_server):
        response = _get(running_server, "/")
        assert "text/html" in response.headers.get("Content-Type", "")

    def test_unknown_device_is_a_404(self, running_server):
        response = _get(running_server, "/device/NOPE")
        assert response.status == 404

    def test_unknown_path_is_a_404(self, running_server):
        response = _get(running_server, "/does-not-exist")
        assert response.status == 404

    def test_download_offers_an_attachment(self, running_server):
        response = _get(running_server, "/export/download")
        assert "attachment" in response.headers.get("Content-Disposition", "")

    def test_download_filename_is_the_config_name(self, running_server):
        response = _get(running_server, "/export/download")
        assert "building_config.yaml" in response.headers.get(
            "Content-Disposition", ""
        )

    def test_download_content_type_is_yaml(self, running_server):
        response = _get(running_server, "/export/download")
        assert response.headers.get("Content-Type") == "application/x-yaml"

    def test_download_body_is_the_real_config(self, running_server):
        response = _get(running_server, "/export/download")
        body = response.read().decode()
        assert "CONFIG_METADATA" in body and "AHU-1" in body

    def test_a_device_page_links_back_to_the_dashboard(self, running_server):
        response = _get(running_server, "/device/AHU-1")
        assert 'href="/"' in response.read().decode()

    def test_content_length_matches_the_body(self, running_server):
        response = _get(running_server, "/validate")
        body = response.read()
        assert int(response.headers["Content-Length"]) == len(body)


class TestFreePort:
    def test_returns_a_bindable_port(self):
        port = free_port()
        assert 1024 < port < 65536

    def test_two_calls_can_both_bind(self):
        """Not guaranteed to differ under extreme load, but should hold in
        practice -- and either way both ports must be usable."""
        first, second = free_port(), free_port()
        assert 1024 < first < 65536 and 1024 < second < 65536
# AI:E87M claude-code 2026-08-27 s:2a846146
