from __future__ import annotations

import logging

from jsonpath_ng.ext import parse

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)
PAGE_TITLE_AST_PATH = '$[?(@.type == "heading" & @.attrs.level == 1 & @.children[0].type == "text")].children[0].raw'


def title(glob_pattern: str, ast_pattern: str | None = None) -> None:
    """
    Sets titles for markdown files that don't have a `title` field in their frontmatter.
    Uses the first # h1 as the title if ast_pattern is not provided. If no # h1 is found,
    the filename is used with the following rules:

    - Replace .md with empty string
    - Replace - with spaces
    - Capitalize

    Args:
        glob_pattern: The glob pattern of the markdown files to update.
        ast_pattern: The jmespath expression to select the title.
            Defaults to the first # h1.
    """
    ast_pattern = ast_pattern or PAGE_TITLE_AST_PATH

    def _default_title(md_file: MarkdownFile, ast_pattern: str) -> str:
        """
        Get the default title for this page.

        Args:
            md_file: The markdown file to get the title for.
            ast_pattern: The jmespath expression to select the title.
                Defaults to the first # h1.

        Returns:
            The default title
        """
        if headers := parse(ast_pattern).find(md_file.ast()):
            return headers[0].value
        return md_file.path.stem.replace("-", " ").capitalize()

    def _title(md_file: MarkdownFile, _) -> None:
        if not "title" in md_file.frontmatter():
            title = _default_title(md_file, ast_pattern)
            md_file.update_frontmatter({"title": title})
            logger.debug(f"Set title: {md_file.path.absolute()}")

    transform(glob_pattern, _title)
