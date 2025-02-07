import logging
from pathlib import Path
from xml.etree import ElementTree as ET

from markupdown.util import resolve_base

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def sitemap(
    glob_pattern: str,
    site_url: str,
    dest_dir: Path | str | None = None,
    default_priority: float = 0.5,
    default_changefreq: str = "weekly",
) -> None:
    """
    Generate a sitemap.xml from markdown files matching a glob pattern.

    Args:
        glob_pattern: The glob pattern to match markdown files to include in the sitemap.
        site_url: Base URL of the website (e.g., 'https://example.com').
        dest_dir: Directory to write the sitemap to.
            Defaults to the base directory of the glob pattern.
        default_priority: Default priority for URLs (0.0 to 1.0).
        default_changefreq: Default change frequency.
            Options: always, hourly, daily, weekly, monthly, yearly, never.
    """
    base_dir, _ = resolve_base(glob_pattern)
    dest_dir = Path(dest_dir) if dest_dir else base_dir

    # Create the root element
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    def _add_url(md_file: MarkdownFile, base_dir: Path) -> None:
        frontmatter = md_file.frontmatter()
        url = ET.SubElement(urlset, "url")

        # Add location
        loc = ET.SubElement(url, "loc")
        loc.text = f"{site_url}/{md_file.url_path(base_dir)}"

        # Add last modified date if available
        if updated_at := frontmatter.get("updated_at"):
            lastmod = ET.SubElement(url, "lastmod")
            lastmod.text = str(updated_at)

        # Add change frequency
        changefreq = ET.SubElement(url, "changefreq")
        changefreq.text = str(frontmatter.get("changefreq", default_changefreq))

        # Add priority
        priority = ET.SubElement(url, "priority")
        priority.text = str(frontmatter.get("priority", default_priority))
        logger.info(f"Added {md_file.path.absolute()}")

    transform(glob_pattern, _add_url)

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(dest_dir / "sitemap.xml", encoding="utf-8", xml_declaration=True)
