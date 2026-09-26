"""A local browser dashboard over the same four functions the CLI calls.

Typing ``python -m bms_dbo validate`` and reading a list of ``[ERROR]`` lines
is a fine workflow for a developer. It is not a good one for the person who
actually knows the building -- a commissioning engineer, a product manager
sitting next to them, anyone who wants to click a device and see what is
wrong with it rather than grep a terminal.

This module serves the same site through a browser instead::

    python -m bms_dbo serve

Design choices, on purpose:

* Stdlib only. No Flask, no template engine, no build step -- this stays a
  ``pip install pyyaml`` away from running on anyone's machine.
* Read-only. Nothing here writes to your CSVs. It is a viewer over
  ``suggest_types`` / ``validate_site`` / ``build_config``, not an editor.
* The site is re-read from disk on every request. Edit a CSV, hit refresh in
  the browser, see the new validation result -- no restart. The ontology is
  loaded once at startup, since it does not change while the server runs.
* Routing and HTML generation live in ``webui_render.py`` as plain functions
  of ``(ontology, site, ...) -> str``. This module is only the HTTP plumbing
  around them, so it stays testable without opening a socket except in the
  handful of tests that specifically exercise the socket layer.
"""

from __future__ import annotations

import http.server
import socket
import webbrowser
from pathlib import Path
from urllib.parse import unquote

from .exporter import build_config, dump_config
from .loader import LoaderError, load_site
from .ontology import Ontology
from .webui_render import (
    page,
    render_dashboard,
    render_device,
    render_export,
    render_not_found,
    render_ontology,
    render_site_error,
    render_validate,
)

DOWNLOAD_PATH = "/export/download"


def route(
    ontology: Ontology,
    pin: dict,
    site_dir: Path,
    raw_path: str,
) -> tuple[int, str, str]:
    """Resolve one request path to ``(status, active_nav, body_html)``.

    Pure and side-effect-free apart from reading the site off disk, which is
    the deliberate "always fresh" behaviour described in the module
    docstring. Kept separate from :class:`DemoHandler` so routing can be unit
    tested without opening a socket.
    """
    path = unquote(raw_path.split("?", 1)[0]).rstrip("/") or "/"

    try:
        site = load_site(site_dir)
    except LoaderError as error:
        return 500, "", render_site_error(error)

    if path == "/":
        return 200, "", render_dashboard(ontology, pin, site)
    if path == "/validate":
        return 200, "validate", render_validate(ontology, site)
    if path in ("/export", DOWNLOAD_PATH):
        return 200, "export", render_export(ontology, site)
    if path == "/ontology":
        return 200, "ontology", render_ontology(ontology, pin)
    if path.startswith("/device/"):
        code = path[len("/device/") :]
        body = render_device(ontology, site, code)
        if body is None:
            return 404, "", render_not_found(path)
        return 200, "", body
    return 404, "", render_not_found(path)


class DemoHandler(http.server.BaseHTTPRequestHandler):
    """Thin HTTP layer: delegate everything to :func:`route`.

    Class attributes ``ontology`` / ``pin`` / ``site_dir`` are injected by
    :func:`make_server`, since ``http.server`` instantiates a fresh handler
    per request and offers no constructor hook of its own.
    """

    ontology: Ontology
    pin: dict
    site_dir: Path

    def log_message(self, format: str, *args) -> None:  # noqa: A002
        pass  # keep the terminal quiet; unhandled errors still raise and log

    def _send_html(self, status: int, active: str, body_html: str) -> None:
        title = {200: "OK", 404: "Not found", 500: "Error"}.get(status, "")
        encoded = page(title, active, body_html).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _send_download(self) -> bool:
        """Stream the config as an attachment. Returns False on error, so the
        caller can fall through to the normal HTML error page."""
        try:
            site = load_site(self.site_dir)
        except LoaderError:
            return False
        text = dump_config(build_config(self.ontology, site))
        encoded = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/x-yaml")
        self.send_header(
            "Content-Disposition", 'attachment; filename="building_config.yaml"'
        )
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        return True

    def do_GET(self) -> None:  # noqa: N802 - stdlib hook name
        if self.path == DOWNLOAD_PATH and self._send_download():
            return
        status, active, body_html = route(
            self.ontology, self.pin, self.site_dir, self.path
        )
        self._send_html(status, active, body_html)


def make_server(
    ontology: Ontology, pin: dict, site_dir: Path, host: str, port: int
) -> http.server.ThreadingHTTPServer:
    """Build a bound (not yet serving) server.

    Split out so tests can pick a free port with ``port=0`` and read it back
    from ``server.server_port`` rather than guessing one and racing it.
    """
    handler = type(
        "BoundDemoHandler",
        (DemoHandler,),
        {"ontology": ontology, "pin": pin, "site_dir": Path(site_dir)},
    )
    return http.server.ThreadingHTTPServer((host, port), handler)


def serve(
    ontology: Ontology,
    pin: dict,
    site_dir: Path,
    host: str = "127.0.0.1",
    port: int = 8765,
    open_tab: bool = True,
) -> None:
    """Serve forever. This is the CLI's ``serve`` command."""
    server = make_server(ontology, pin, site_dir, host, port)
    url = f"http://{host}:{server.server_port}/"
    print(f"Serving the DBO demo dashboard at {url}")
    print("Edit the CSVs in", site_dir, "and refresh the browser to see changes.")
    print("Press Ctrl+C to stop.")
    if open_tab:
        try:
            webbrowser.open(url)
        except (webbrowser.Error, OSError) as error:
            print(f"(could not open a browser tab automatically: {error})")
            print(f"Open {url} yourself.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        server.server_close()


def free_port() -> int:
    """An unused localhost port, for tests that need a real socket."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]
# AI:E87M claude-code 2026-08-27 s:2a846146
