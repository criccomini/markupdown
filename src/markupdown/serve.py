from __future__ import annotations

import logging
import subprocess
from pathlib import Path

from livereload import Server

logger = logging.getLogger(__name__)


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
    server = Server()

    # Watch the directories for changes and run build script
    for watch_dir in watch_dirs:
        server.watch(str(watch_dir), rebuild)

    # Serve the site directory
    server.serve(root=site_dir, port=port, restart_delay=1)
