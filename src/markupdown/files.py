from __future__ import annotations

import copy
from pathlib import Path

import frontmatter
import mistune

AST_RENDERER = mistune.create_markdown(renderer=None)


class MarkdownFile:
    path: Path
    _post: frontmatter.Post
    _ast: list[dict[str, object]]
    _modified: bool

    def __init__(self, path: Path | str) -> None:
        self.path = Path(path).resolve().absolute()
        self._modified = False

        # Load frontmatter and content
        with open(self.path, "r", encoding="utf-8") as f:
            self._post = frontmatter.load(f)

        # Load markdown AST
        ast = AST_RENDERER(self.content())
        assert isinstance(ast, list)
        self._ast = ast

    def frontmatter(self) -> dict[str, object]:
        return copy.deepcopy(self._post.metadata)

    def content(self) -> str:
        return self._post.content

    def ast(self) -> list[dict[str, object]]:
        return self._ast

    def set_content(self, content: str) -> None:
        self._post.content = content
        self._modified = True

    def update_frontmatter(self, metadata: dict[str, object]) -> None:
        self._post.metadata.update(metadata)
        self._modified = True

    def del_frontmatter_key(self, key: str) -> None:
        self._post.metadata.pop(key)
        self._modified = True

    def url_path(self, base_dir: Path | str) -> str:
        """
        Returns the URL path of the current page relative to the base directory.

        For example, if we have:

        - self.path: /home/alice/blog/posts/this-post.md
        - base_dir: /home/alice/blog

        The returned URL is /posts/this-post

        Args:
            base_dir: The base directory to resolve the link against.

        Returns:
            The URL of the current page relative to the base directory.
        """
        link_path = self.subpath(base_dir)
        link_path = link_path.with_suffix("")
        if link_path.name == "index":
            link_path = link_path.parent
        return link_path.as_posix()

    def resolve(self, base_dir: Path | str, rel_path: Path | str) -> Path:
        """
        Converts a path relative to the current markdown file into a subpath
        relative to the base directory. For example, if we have:

        - self.path: /home/alice/blog/posts/this-post.md
        - base_dir: /home/alice/blog
        - rel_path: ../index.md

        The returned path is index.md

        Args:
            base_dir: The base directory to resolve the link against.
            rel_path: The relative path to resolve.

        Returns:
            The absolute path of the relative path.
        """
        base_dir = Path(base_dir).resolve().absolute()
        rel_path = Path(rel_path)
        abs_path = (
            (self.path.parent / rel_path).resolve().absolute().relative_to(base_dir)
        )
        return abs_path

    def subpath(self, base_dir: Path | str) -> Path:
        """
        Returns the path of the current page relative to the base directory.

        For example, if we have:

        - self.path: /home/alice/blog/posts/this-post.md
        - base_dir: /home/alice/blog

        The returned path is posts/this-post.md

        Args:
            base_dir: The base directory to resolve the link against.

        Returns:
            The path of the current page relative to the base directory.
        """
        base_dir = Path(base_dir).resolve().absolute()
        return self.path.relative_to(base_dir)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self._modified:
            with open(self.path, "wb") as f:
                frontmatter.dump(self._post, f)
        elif not self.path.exists():
            # Create empty file if it doesn't exist and we haven't modified it
            self.path.touch()
