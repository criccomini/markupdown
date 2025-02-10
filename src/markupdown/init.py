from __future__ import annotations

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def init(root_path: Path | str = ".", safety: bool = True) -> None:
    """
    Initialize a new markupdown project by copying the example directory structure.

    Args:
        root_path: The target directory where the example should be copied.
            Defaults to current directory.
        safety: Confirms if the target directory is not empty before initializing.
            Defaults to True.
    """
    # Get the example directory path
    root_path = Path(root_path)

    # Check if directory exists and has contents
    if (
        safety
        and root_path.exists()
        and root_path.is_dir()
        and any(root_path.iterdir())
    ):
        confirm = input(f"Directory {root_path} is not empty. Continue? (y/N) ")
        if confirm.lower() not in ["y", "yes"]:
            return

    # Find the example directory
    pkg_dir = Path(__file__).absolute().parent
    while pkg_dir.exists() and not (pkg_dir / "example").is_dir():
        pkg_dir = pkg_dir.parent

    if not pkg_dir.exists():
        raise ValueError(f"Example directory not found in path of {pkg_dir}")

    example_dir = pkg_dir / "example"

    # Copy example directory structure
    shutil.copytree(example_dir, root_path, dirs_exist_ok=True)

    logger.debug(f"Initialized new markupdown project in {root_path.absolute()}")
