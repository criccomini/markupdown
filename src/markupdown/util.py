import logging
import logging.config
import os
from html.parser import HTMLParser
from io import StringIO
from pathlib import Path

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "INFO",
        },
    },
    "loggers": {
        "markupdown": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


def init_logger() -> None:
    if not logging.getLogger("markupdown").handlers:
        logging.config.dictConfig(LOGGING_CONFIG)


def resolve_base(glob_pattern: str) -> tuple[Path, str]:
    """
    Given a glob pattern, resolve the base directory and relative glob pattern.

    Some examples:

    - "site/**/*.md" -> ("site", "**/*.md")
    - "**/*.md" -> (current directory, "**/*.md")
    - "post[s]/index.md" -> (current directory, "post[s]/index.md")
    - "/pages/post[s]/index.md" -> ("/pages", "post[s]/index.md")
    """
    p = Path(glob_pattern)
    safe_parts = []

    for part in p.parts:
        if any(ch in part for ch in "*?["):
            break
        safe_parts.append(part)

    if not safe_parts:
        base = Path.cwd()
        glob_part = glob_pattern
    else:
        base = Path(*safe_parts)
        remainder_parts = p.parts[len(safe_parts) :]
        glob_part = os.path.join(*remainder_parts) if remainder_parts else ""

    return base.absolute(), glob_part


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data: str):
        self.text.write(data)

    def get_data(self):
        return self.text.getvalue()


def strip_html(html: str) -> str:
    s = HTMLStripper()
    s.feed(html)
    return s.get_data().strip()
