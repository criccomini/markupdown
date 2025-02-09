from __future__ import annotations

import logging
from pathlib import Path

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def link(glob_pattern: str) -> None:
    """
    Sets the 'link' field in frontmatter for markdown files matching the glob pattern.
    The link is constructed from the file path, with special handling for index.md files.
    The path will be a relative path from the base directory of the glob pattern.

    Args:
        glob_pattern: The glob pattern to match markdown files to update.
    """

    def _link(md_file: MarkdownFile, base_dir: Path) -> None:
        link = Path("/") / md_file.url_path(base_dir=base_dir)
        md_file.update_frontmatter({"link": link.as_posix()})
        logger.debug(f"Set link: {md_file.path.absolute()}")

    transform(glob_pattern, _link)
