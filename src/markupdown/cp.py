from __future__ import annotations

import logging
import shutil
from pathlib import Path

from .ls import ls

logger = logging.getLogger(__name__)


def cp(
    glob_pattern: str,
    dest_dir: Path | str,
) -> None:
    """
    Copy files matching a glob pattern to a destination directory. If the file is a markdown
    file, a `source` field will be added to the frontmatter in the copied file.

    Args:
        glob_pattern: The glob pattern to match files to copy.
        dest_dir: The destination directory to copy files to.
    """
    base_dir, subpaths = ls(glob_pattern)
    dest_dir = Path(dest_dir).absolute()

    for subpath in subpaths:
        src_file = base_dir / subpath
        dest_file = dest_dir / subpath

        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dest_file)
        logger.debug(f"Copied {src_file} to {dest_file}")
