from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

from git import Commit, InvalidGitRepositoryError, Repo

from .files import MarkdownFile
from .transform import transform

logger = logging.getLogger(__name__)


def changelog(
    glob_pattern: str = "**/*.md",
    dest_dir: Path | str | None = None,
) -> None:
    """
    Add git metadata to markdown frontmatter in files matching a glob pattern. Adds:

        - created_at
        - updated_at
        - changelog

    The changelog field is a list of dictionaries with the following keys:

        - hash: The commit hash
        - author: The commit author
        - date: The commit date
        - message: The commit message

    Args:
        glob_pattern: The glob pattern to match markdown files to update.
        dest_dir: Base directory of markdown files that should be updated.
            Not necessarily the same as the base directory of the glob pattern since
            you might wish to get changelogs from source files in a git managed
            content directory and apply them to a site directory that isn't in git.
    """

    def _commit_info(commit: Commit) -> dict[str, str]:
        tz_created = timezone(timedelta(seconds=commit.committer_tz_offset))
        created_at = datetime.fromtimestamp(
            commit.committed_date, tz_created
        ).isoformat()

        return {
            "hash": str(commit.hexsha),
            "author": str(commit.author.name),
            "date": created_at,
            "message": str(commit.message.strip()),
        }

    def _changelog(md_file: MarkdownFile, base_dir: Path) -> None:
        try:
            repo = Repo(md_file.path, search_parent_directories=True)
        except InvalidGitRepositoryError:
            logger.warning(f"Skipping changelog for non git repository: {md_file.path}")
            return
        commits = list(repo.iter_commits(paths=md_file.path))

        if commits:
            # Use committer_tz_offset to get the commit date in the file's timezone
            # The oldest commit (created_at) and the newest commit (updated_at)
            created_at = _commit_info(commits[-1])["date"]
            updated_at = _commit_info(commits[0])["date"]
            changelog = []

            for commit in commits:
                changelog.append(_commit_info(commit))

            file_to_update = md_file
            if dest_dir:
                file_to_update = MarkdownFile(
                    dest_dir / md_file.path.relative_to(base_dir)
                )
            metadata = file_to_update.frontmatter()
            metadata.setdefault("changelog", [])
            metadata.setdefault("created_at", created_at)
            metadata.setdefault("updated_at", updated_at)
            metadata["changelog"] = changelog
            file_to_update.update_frontmatter(metadata)
            file_to_update.save()
            logger.debug(f"Set changelog: {file_to_update.path.absolute()}")

    transform(glob_pattern, _changelog)
