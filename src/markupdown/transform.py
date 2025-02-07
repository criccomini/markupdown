from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from .files import MarkdownFile
from .ls import ls


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

    for subpath in subpaths:
        path = base_dir / subpath
        if path.is_file():
            md_file = MarkdownFile(path)
            func(md_file, base_dir)
            md_file.save()
