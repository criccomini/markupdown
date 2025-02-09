import logging
from pathlib import Path

from jsonpath_ng.ext import parse

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)
A_HREF_AST_PATH = "$..attrs.url"


def references(glob_pattern: str, ast_pattern: str | None = None) -> None:
    ast_pattern = ast_pattern or A_HREF_AST_PATH

    def _references(md_file: MarkdownFile, base_dir: Path) -> None:
        referencer_path = md_file.subpath(base_dir)
        references = parse(ast_pattern).find(md_file.ast())
        references = filter(lambda r: r.value.endswith(".md"), references)
        references = [reference.value for reference in references]
        references = [
            str(md_file.resolve(base_dir, reference)) for reference in references
        ]

        for reference in references:
            referenced_md = MarkdownFile(base_dir / reference)
            backreferences = referenced_md.frontmatter().get("backreferences") or []
            assert isinstance(backreferences, list)
            backreferences.append(str(referencer_path))
            referenced_md.update_frontmatter({"backreferences": backreferences})
            referenced_md.save()

        if references:
            md_file.update_frontmatter({"references": references})
            logger.debug(f"Set references for {md_file.path}")

    transform(glob_pattern, _references)
