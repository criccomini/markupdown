from __future__ import annotations

import logging
from pathlib import Path

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def siblings(glob_pattern: str) -> None:
    def _siblings(md_file: MarkdownFile, base_dir: Path) -> None:
        dir_path = md_file.path.parent.absolute()
        siblings = []

        for sibling in (dir_path).glob("*.md"):
            if md_file.path.name == sibling.name:
                continue

            sibling_md = MarkdownFile(dir_path / sibling.name)

            siblings.append(str(sibling_md.subpath(base_dir)))

        if siblings:
            md_file.update_frontmatter({"siblings": siblings})
            logger.debug(f"Set siblings for {md_file.path}")

    transform(glob_pattern, _siblings)
