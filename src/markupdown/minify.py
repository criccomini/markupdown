import logging

import minify_html

from .ls import ls

logger = logging.getLogger(__name__)


def minify(
    glob_pattern: str,
) -> None:
    """
    Minify HTML, CSS, and JS files matching a glob pattern.

    Args:
        glob_pattern: The glob pattern to match HTML, CSS, and JS files to minify.
    """
    base_dir, subpaths = ls(glob_pattern)

    for subpath in subpaths:
        path = base_dir / subpath
        if path.is_file():
            html = path.read_text()
            minified = minify_html.minify(
                html,
                do_not_minify_doctype=True,
                ensure_spec_compliant_unquoted_attribute_values=True,
                keep_spaces_between_attributes=True,
                keep_html_and_head_opening_tags=True,
                minify_css=True,
                minify_js=True,
            )
            path.write_text(minified)
            logger.info(f"Minified {path}")
