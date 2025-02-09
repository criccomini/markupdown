import logging
from datetime import datetime, timezone
from pathlib import Path

from feedgen.feed import FeedGenerator

from markupdown.util import resolve_base

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def feed(
    glob_pattern: str,
    feed_id: str,
    feed_title: str,
    feed_link: str,
    feed_description: str,
    feed_author: str | None = None,
    dest_dir: Path | str | None = None,
) -> None:
    """
    Generate an RSS feed from markdown files matching a glob pattern.

    Args:
        glob_pattern: The glob pattern to match markdown files to include in the feed.
        dest_dir: Directory to write the RSS feed to.
            Defaults to the base directory of the glob pattern.
        feed_title: Title of the RSS feed. Defaults to "Blog Feed".
        feed_link: Link to the website. Defaults to "http://example.com".
        feed_description: Description of the feed. Defaults to "Latest blog posts".
    """
    fg = FeedGenerator()
    fg.id(feed_id)
    fg.author(feed_author)
    fg.title(feed_title)
    fg.link(href=feed_link, rel="alternate")
    fg.description(feed_description)
    fg.language("en")
    fg.updated(datetime.now(timezone.utc))

    def _add_entry(md_file: MarkdownFile, base_dir: Path) -> None:
        frontmatter = md_file.frontmatter()

        entry = fg.add_entry()
        entry.title(frontmatter.get("title", md_file.path.stem))

        if date := frontmatter.get("created_at"):
            entry.published(date)

        link = f"{feed_link}/{md_file.url_path(base_dir)}"
        entry.link(href=link)
        entry.id(link)

        description = frontmatter.get("description", md_file.content().split("\n\n")[0])
        entry.description(description)

    transform(glob_pattern, _add_entry)

    if dest_dir is None:
        dest_dir, _ = resolve_base(glob_pattern)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)

    fg.rss_file(str(dest_dir / "rss.xml"), pretty=True)
    logger.debug(f"Generated RSS feed: {dest_dir / 'rss.xml'}")
    fg.atom_file(str(dest_dir / "atom.xml"), pretty=True)
    logger.debug(f"Generated Atom feed: {dest_dir / 'atom.xml'}")
