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
        dest_file_or_dir = dest_dir / subpath
        dest_file_or_dir.parent.mkdir(parents=True, exist_ok=True)
        if src_file.is_dir():
            shutil.copytree(src_file, dest_file_or_dir, dirs_exist_ok=True)
        else:
            shutil.copy2(src_file, dest_file_or_dir)
        logger.debug(f"Copied {src_file} to {dest_file_or_dir}")
