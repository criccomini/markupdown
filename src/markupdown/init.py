from __future__ import annotations

import logging
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)


def init(root_path: Path | str = ".") -> None:
    """
    Initialize a new markupdown project by copying the example directory structure.

    Args:
        root_path: The target directory where the example should be copied.
            Defaults to current directory.
    """
    # Get the example directory path
    root_path = Path(root_path)

    # Find the example directory
    pkg_dir = Path(__file__).absolute().parent
    while pkg_dir.exists() and not (pkg_dir / "example").is_dir():
        pkg_dir = pkg_dir.parent

    if not pkg_dir.exists():
        raise ValueError(f"Example directory not found in path of {pkg_dir}")

    example_dir = pkg_dir / "example"

    # Create root directory if it doesn't exist
    shutil.copytree(example_dir, root_path, dirs_exist_ok=True)

    logger.debug(f"Initialized new markupdown project in {root_path.absolute()}")
