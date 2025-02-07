from __future__ import annotations

from pathlib import Path

from .util import resolve_base


def ls(glob_pattern: str) -> tuple[Path, list[Path]]:
    """
    List files matching a glob pattern.

    Args:
        glob_pattern: Relative or absolute glob pattern to match files.

    Returns:
        A tuple containing (base_dir, list_of_matching_subpaths).
    """
    base_dir, glob_pattern = resolve_base(glob_pattern)

    # list() to snapshot the directory contents so we don't go into a recursive loop.
    # not memory efficient, but it fixes the problem.
    subpaths = base_dir.glob(glob_pattern)
    subpaths = map(lambda p: p.relative_to(base_dir), subpaths)
    return base_dir, list(subpaths)
