import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def clean(dir: Path | str | None = None, safety: bool = True):
    """
    Delete the contents of a directory if it exists.

    Args:
        dir: The directory to clean. Defaults to the current directory.
        safety: Confirms if the directory to clean is not under the current directory.
            Defaults to True.
    """
    dir = Path(dir) if dir else Path.cwd()

    if safety and not dir.absolute().is_relative_to(Path.cwd()):
        confirm = input(f"Are you sure you want to clean {dir}? (y/N) ")
        if confirm.lower() not in ["y", "yes"]:
            return

    if dir.exists() and dir.is_dir():
        for item in dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
        logger.debug(f"Cleaned directory contents: {dir}")
    else:
        logger.warning(f"Directory not found: {dir}")
