from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Callable

from .files import MarkdownFile
from .ls import ls

logger = logging.getLogger(__name__)


def transform(
    glob_pattern: str,
    func: Callable[[MarkdownFile, Path], Any],
) -> None:
    """
    Apply a transformation function to markdown files matching a glob pattern.

    Args:
        glob_pattern: The glob pattern to match markdown files to transform.
        func: A callable that takes a MarkdownFile and SiteFile as arguments and applies
            the desired transformation.
    """
    base_dir, subpaths = ls(glob_pattern)

    if not subpaths:
        logger.warning(f"No files found matching {glob_pattern}")

    for subpath in subpaths:
        path = base_dir / subpath
        if path.is_file() and path.exists():
            try:
                md_file = MarkdownFile(path)
                func(md_file, base_dir)
                md_file.save()
            except Exception as e:
                logger.error(f"Failed to transform {path}: {e}")
        else:
            # Skipping func for path
            logger.warning(f"Skipping {func.__name__} for {path}: not a markdown file")
