from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from urllib.parse import unquote

from livereload import Server

logger = logging.getLogger(__name__)


def _make_app(root: Path):
    def application(environ, start_response):
        path = environ.get("PATH_INFO", "/")
        path = unquote(path)
        path = Path(path.strip("/"))

        # Security check: ensure the requested file is relative to current directory
        if path.is_absolute():
            start_response("403 Forbidden", [("Content-Type", "text/plain")])
            return [b"403 Forbidden"]

        path = (root / path).absolute()

        # If the path is a directory, try to serve index.html inside it.
        if path.is_dir():
            path = path / "index.html"
        elif not path.exists() and path.with_suffix(".html").exists():
            path = path.with_suffix(".html")
        elif not path.exists():
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"404 Not Found"]

        # Determine the Content-Type based on file extension.
        content_type = "application/octet-stream"
        if path.suffix == ".html" or path.suffix == ".htm":
            content_type = "text/html"
        elif path.suffix == ".css":
            content_type = "text/css"
        elif path.suffix == ".js":
            content_type = "application/javascript"
        elif path.suffix == ".png":
            content_type = "image/png"
        elif path.suffix == ".jpg" or path.suffix == ".jpeg":
            content_type = "image/jpeg"
        elif path.suffix == ".gif":
            content_type = "image/gif"
        elif path.suffix == ".ico":
            content_type = "image/x-icon"
        elif path.suffix == ".svg":
            content_type = "image/svg+xml"
        elif path.suffix == ".webp":
            content_type = "image/webp"
        elif path.suffix == ".json" or path.suffix == ".jsonl":
            content_type = "application/json"
        elif path.suffix == ".xml":
            content_type = "application/xml"
        elif path.suffix == ".txt":
            content_type = "text/plain"
        elif path.suffix == ".md":
            content_type = "text/markdown"
        elif path.suffix == ".yaml" or path.suffix == ".yml":
            content_type = "text/yaml"
        elif path.suffix == ".toml" or path.suffix == ".tml":
            content_type = "text/toml"

        # Try reading the file in binary mode.
        try:
            with open(path, "rb") as f:
                content = f.read()
        except Exception as e:
            start_response(
                "500 Internal Server Error", [("Content-Type", "text/plain")]
            )
            return [b"500 Internal Server Error"]

        # Send HTTP headers.
        headers = [
            ("Content-Type", content_type),
            ("Content-Length", str(len(content))),
        ]
        start_response("200 OK", headers)
        return [content]

    return application


def serve(
    port: int = 8000,
    build_script: Path | str = "build.py",
    site_dir: Path | str = "site",
    watch_dirs: list[Path | str] = [],
):
    """
    Start a local development server to preview the generated site.
    Uses the build.py script to rebuild the site when changes are detected.

    Args:
        port: The port number to run the server on. Defaults to 8000.
        build_script: The build.py script to use. Defaults to "build.py".
        site_dir: The directory to serve. Defaults to "site".
        watch_dirs: Directories to watch for changes.
            Defaults to ["content", "templates", "assets", "build.py"].
    """
    site_dir = Path(site_dir).absolute()
    build_script = Path(build_script).absolute()
    clean_script = "python -m markupdown clean {}".format(site_dir).split()
    watch_dirs = watch_dirs or ["content", "templates", "assets", "build.py"]

    if not build_script.exists():
        logger.warning(f"build.py not found in {build_script}")
        return

    def rebuild():
        try:
            subprocess.run(clean_script, check=True)
            subprocess.run(["python", str(build_script)], check=True)
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Error during rebuild: {e}")
            return False

    # Initial build
    rebuild()

    # Create livereload server
    server = Server(_make_app(site_dir))

    # Watch the directories for changes and run build script
    for watch_dir in watch_dirs:
        server.watch(str(watch_dir), rebuild)

    # Serve the site directory
    server.serve(port=port, restart_delay=1)
