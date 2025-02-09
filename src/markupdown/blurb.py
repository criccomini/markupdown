from __future__ import annotations

import logging
import re

import mistune

from .files import MarkdownFile
from .transform import transform
from .util import strip_html

logger = logging.getLogger(__name__)

# This regex works in multiline (M) and dot-all (S) mode.
# It says: starting after a blank line or the beginning,
# if the first non-space characters are NOT one of:
#   - a header marker (1–6 '#' characters followed by a space)
#   - a blockquote marker ('>')
#   - a list marker (either '*', '-', '+', or a numbered list like '1.')
# then capture until the next blank line or the end of string.
FIRST_PARAGRAPH_RE = re.compile(
    r"(?s)(?:\A|\n\n)"  # Match start of string or a blank line (non-capturing)
    r"(?![ \t]*(?:#{1,6}\s|>|\* |- |\+ |\d+\.\s))"  # Negative lookahead to skip markdown markers
    r"(.+?)"  # Lazily capture the paragraph text
    r"(?=\n\n|\Z)"  # Stop at the next blank line or the end of the string
)


def blurb(
    glob_pattern: str,
    max_length: int = 200,
) -> None:
    """
    Sets blurb for markdown files that don't have a `blurb` field in their frontmatter.
    Uses the first non-heading paragraph as the blurb if ast_pattern is not provided.
    """

    def _blurb(md_file: MarkdownFile, _) -> None:
        if "blurb" in md_file.frontmatter():
            return
        if paragraphs := FIRST_PARAGRAPH_RE.findall(md_file.content()):
            blurb = paragraphs[0]
            blurb = str(mistune.html(blurb))
            blurb = strip_html(blurb)
            if max_length and len(blurb) > max_length:
                # Trim blurb to max_length -3 and walk backwards until a space is found
                blurb = blurb[: max_length - 3]
                while not blurb[-1].isspace():
                    blurb = blurb[:-1]
                blurb += "..."
            md_file.update_frontmatter({"blurb": blurb})
            logger.debug(f"Set blurb: {md_file.path.absolute()}")
        else:
            logger.warning(f"Could not find blurb: {md_file.path.absolute()}")

    transform(glob_pattern, _blurb)
