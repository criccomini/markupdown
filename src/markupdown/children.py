from __future__ import annotations

import logging
from pathlib import Path

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def children(glob_pattern: str) -> None:
    def _children(md_file: MarkdownFile, base_dir: Path) -> None:
        dir_path = md_file.path.parent.absolute()
        children = []

        for child in dir_path.iterdir():
            if not child.is_dir():
                continue

            index_dir_path = dir_path / child
            index_md_path = index_dir_path / "index.md"

            if not index_md_path.is_file():
                continue

            index_md = MarkdownFile(index_md_path)
            children.append(str(index_md.subpath(base_dir)))

        if children:
            md_file.update_frontmatter({"children": children})
            logger.info(f"Set children for {md_file.path}")

    transform(glob_pattern, _children)
