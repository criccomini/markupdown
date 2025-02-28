from __future__ import annotations

import logging

import mistune
from mistune.toc import add_toc_hook

from .files import MarkdownFile
from .render import TocHeadingGenerator
from .transform import transform

logger = logging.getLogger(__name__)


def toc(glob_pattern: str) -> None:
    """
    Sets the 'toc' field in frontmatter for markdown files matching the glob pattern.
    The 'toc' field is a list of dicts with the following keys:
        - 'level': The heading level
        - 'slug': The slug of the heading
        - 'title': The text of the heading

    Args:
        glob_pattern: The glob pattern to match markdown files to update.
    """

    def _toc(md_file: MarkdownFile, _) -> None:
        md = mistune.create_markdown()
        add_toc_hook(md, heading_id=TocHeadingGenerator())
        _, state = md.parse(md_file.content())
        toc_items = state.env["toc_items"]
        toc_items = [
            dict(level=level, slug=slug, title=title)
            for level, slug, title in toc_items
        ]
        md_file.update_frontmatter({"toc": toc_items})
        logger.debug(f"Set toc: {md_file.path.absolute()}")

    transform(glob_pattern, _toc)
