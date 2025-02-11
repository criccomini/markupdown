# Documentation

## Table of Contents

- [`markupdown`](#markupdown)
- [`__main__`](#main)
- [`blurb`](#blurb)
  - [`blurb.blurb`](#blurb-blurb)
- [`changelog`](#changelog)
  - [`changelog.changelog`](#changelog-changelog)
- [`children`](#children)
  - [`children.children`](#children-children)
- [`clean`](#clean)
  - [`clean.clean`](#clean-clean)
- [`cp`](#cp)
  - [`cp.cp`](#cp-cp)
- [`feed`](#feed)
  - [`feed.feed`](#feed-feed)
- [`files`](#files)
  - [`files.MarkdownFile`](#files-markdownfile)
    - [`files.MarkdownFile.__init__`](#files-markdownfile-init)
    - [`files.MarkdownFile.frontmatter`](#files-markdownfile-frontmatter)
    - [`files.MarkdownFile.content`](#files-markdownfile-content)
    - [`files.MarkdownFile.ast`](#files-markdownfile-ast)
    - [`files.MarkdownFile.set_content`](#files-markdownfile-set-content)
    - [`files.MarkdownFile.update_frontmatter`](#files-markdownfile-update-frontmatter)
    - [`files.MarkdownFile.del_frontmatter_key`](#files-markdownfile-del-frontmatter-key)
    - [`files.MarkdownFile.url_path`](#files-markdownfile-url-path)
    - [`files.MarkdownFile.resolve`](#files-markdownfile-resolve)
    - [`files.MarkdownFile.subpath`](#files-markdownfile-subpath)
    - [`files.MarkdownFile.save`](#files-markdownfile-save)
- [`init`](#init)
  - [`init.init`](#init-init)
- [`link`](#link)
  - [`link.link`](#link-link)
- [`ls`](#ls)
  - [`ls.ls`](#ls-ls)
- [`minify`](#minify)
  - [`minify.minify`](#minify-minify)
- [`pydoc`](#pydoc)
  - [`pydoc.make_anchor`](#pydoc-make-anchor)
  - [`pydoc.add_header`](#pydoc-add-header)
  - [`pydoc.get_module_name`](#pydoc-get-module-name)
  - [`pydoc.extract_all_from_ast`](#pydoc-extract-all-from-ast)
  - [`pydoc.get_function_signature`](#pydoc-get-function-signature)
  - [`pydoc.format_docstring`](#pydoc-format-docstring)
  - [`pydoc.extract_docstrings_from_node`](#pydoc-extract-docstrings-from-node)
  - [`pydoc.process_file`](#pydoc-process-file)
  - [`pydoc.crawl_directory`](#pydoc-crawl-directory)
  - [`pydoc.generate_toc`](#pydoc-generate-toc)
  - [`pydoc.generate_exports_section`](#pydoc-generate-exports-section)
  - [`pydoc.main`](#pydoc-main)
- [`references`](#references)
  - [`references.references`](#references-references)
- [`render`](#render)
  - [`render.MarkupdownRenderer`](#render-markupdownrenderer)
    - [`render.MarkupdownRenderer.__init__`](#render-markupdownrenderer-init)
    - [`render.MarkupdownRenderer.link`](#render-markupdownrenderer-link)
    - [`render.MarkupdownRenderer.block_code`](#render-markupdownrenderer-block-code)
  - [`render.render`](#render-render)
- [`serve`](#serve)
  - [`serve.serve`](#serve-serve)
- [`siblings`](#siblings)
  - [`siblings.siblings`](#siblings-siblings)
- [`sitemap`](#sitemap)
  - [`sitemap.sitemap`](#sitemap-sitemap)
- [`title`](#title)
  - [`title.title`](#title-title)
- [`transform`](#transform)
  - [`transform.transform`](#transform-transform)
- [`util`](#util)
  - [`util.init_logger`](#util-init-logger)
  - [`util.resolve_base`](#util-resolve-base)
  - [`util.HTMLStripper`](#util-htmlstripper)
    - [`util.HTMLStripper.__init__`](#util-htmlstripper-init)
    - [`util.HTMLStripper.handle_data`](#util-htmlstripper-handle-data)
    - [`util.HTMLStripper.get_data`](#util-htmlstripper-get-data)
  - [`util.strip_html`](#util-strip-html)

## Exports

- [`markupdown`](#markupdown):
  - [`blurb`](#blurb-blurb)
  - [`changelog`](#changelog-changelog)
  - [`children`](#children-children)
  - [`clean`](#clean-clean)
  - [`cp`](#cp-cp)
  - [`feed`](#feed-feed)
  - [`init`](#init-init)
  - [`link`](#link-link)
  - [`ls`](#ls-ls)
  - [`minify`](#minify-minify)
  - [`references`](#references-references)
  - [`render`](#render-render)
  - [`serve`](#serve-serve)
  - [`siblings`](#siblings-siblings)
  - [`sitemap`](#sitemap-sitemap)
  - [`title`](#title-title)
  - [`transform`](#transform-transform)

<a id="markupdown"></a>
# `markupdown`


<a id="main"></a>
# `__main__`


<a id="blurb"></a>
# `blurb`

<a id="blurb-blurb"></a>
## `blurb.blurb`

```python
def blurb(glob_pattern: str, max_length: int) -> None:
```

Sets blurb for markdown files that don't have a `blurb` field in their frontmatter.

Uses the first non-heading paragraph as the blurb if ast_pattern is not provided.



<a id="changelog"></a>
# `changelog`

<a id="changelog-changelog"></a>
## `changelog.changelog`

```python
def changelog(glob_pattern: str, dest_dir: Path | str | None) -> None:
```

Add git metadata to markdown frontmatter in files matching a glob pattern. Adds:

- created_at
    - updated_at
    - changelog

The changelog field is a list of dictionaries with the following keys:

    - hash: The commit hash
    - author: The commit author
    - date: The commit date
    - message: The commit message

**Args:**

- `glob_pattern`: The glob pattern to match markdown files to update.
- `dest_dir`: Base directory of markdown files that should be updated.
Not necessarily the same as the base directory of the glob pattern since
you might wish to get changelogs from source files in a git managed
content directory and apply them to a site directory that isn't in git.



<a id="children"></a>
# `children`

<a id="children-children"></a>
## `children.children`

```python
def children(glob_pattern: str) -> None:
```


<a id="clean"></a>
# `clean`

<a id="clean-clean"></a>
## `clean.clean`

```python
def clean(dir: Path | str | None, safety: bool):
```

Delete the contents of a directory if it exists.

**Args:**

- `dir`: The directory to clean. Defaults to the current directory.
- `safety`: Confirms if the directory to clean is not under the current directory.
Defaults to True.



<a id="cp"></a>
# `cp`

<a id="cp-cp"></a>
## `cp.cp`

```python
def cp(glob_pattern: str, dest_dir: Path | str) -> None:
```

Copy files matching a glob pattern to a destination directory. If the file is a markdown

file, a `source` field will be added to the frontmatter in the copied file.

**Args:**

- `glob_pattern`: The glob pattern to match files to copy.
- `dest_dir`: The destination directory to copy files to.



<a id="feed"></a>
# `feed`

<a id="feed-feed"></a>
## `feed.feed`

```python
def feed(glob_pattern: str, feed_id: str, feed_title: str, feed_link: str, feed_description: str, feed_author: str | None, dest_dir: Path | str | None) -> None:
```

Generate an RSS feed from markdown files matching a glob pattern.

**Args:**

- `glob_pattern`: The glob pattern to match markdown files to include in the feed.
- `dest_dir`: Directory to write the RSS feed to.
Defaults to the base directory of the glob pattern.
- `feed_title`: Title of the RSS feed. Defaults to "Blog Feed".
- `feed_link`: Link to the website. Defaults to "http://example.com".
- `feed_description`: Description of the feed. Defaults to "Latest blog posts".



<a id="files"></a>
# `files`

<a id="files-markdownfile"></a>
## `files.MarkdownFile`

<a id="files-markdownfile-init"></a>
### `files.MarkdownFile.__init__`

```python
def __init__(self, path: Path | str) -> None:
```

<a id="files-markdownfile-frontmatter"></a>
### `files.MarkdownFile.frontmatter`

```python
def frontmatter(self) -> dict[str, object]:
```

<a id="files-markdownfile-content"></a>
### `files.MarkdownFile.content`

```python
def content(self) -> str:
```

<a id="files-markdownfile-ast"></a>
### `files.MarkdownFile.ast`

```python
def ast(self) -> list[dict[str, object]]:
```

<a id="files-markdownfile-set-content"></a>
### `files.MarkdownFile.set_content`

```python
def set_content(self, content: str) -> None:
```

<a id="files-markdownfile-update-frontmatter"></a>
### `files.MarkdownFile.update_frontmatter`

```python
def update_frontmatter(self, metadata: dict[str, object]) -> None:
```

<a id="files-markdownfile-del-frontmatter-key"></a>
### `files.MarkdownFile.del_frontmatter_key`

```python
def del_frontmatter_key(self, key: str) -> None:
```

<a id="files-markdownfile-url-path"></a>
### `files.MarkdownFile.url_path`

```python
def url_path(self, base_dir: Path | str) -> str:
```

Returns the URL path of the current page relative to the base directory.

For example, if we have:

- self.path: /home/alice/blog/posts/this-post.md
- base_dir: /home/alice/blog

The returned URL is /posts/this-post

**Args:**

- `base_dir`: The base directory to resolve the link against.

**Returns:** The URL of the current page relative to the base directory.


<a id="files-markdownfile-resolve"></a>
### `files.MarkdownFile.resolve`

```python
def resolve(self, base_dir: Path | str, rel_path: Path | str) -> Path:
```

Converts a path relative to the current markdown file into a subpath

relative to the base directory. For example, if we have:

- self.path: /home/alice/blog/posts/this-post.md
- base_dir: /home/alice/blog
- rel_path: ../index.md

The returned path is index.md

**Args:**

- `base_dir`: The base directory to resolve the link against.
- `rel_path`: The relative path to resolve.

**Returns:** The absolute path of the relative path.


<a id="files-markdownfile-subpath"></a>
### `files.MarkdownFile.subpath`

```python
def subpath(self, base_dir: Path | str) -> Path:
```

Returns the path of the current page relative to the base directory.

For example, if we have:

- self.path: /home/alice/blog/posts/this-post.md
- base_dir: /home/alice/blog

The returned path is posts/this-post.md

**Args:**

- `base_dir`: The base directory to resolve the link against.

**Returns:** The path of the current page relative to the base directory.


<a id="files-markdownfile-save"></a>
### `files.MarkdownFile.save`

```python
def save(self) -> None:
```


<a id="init"></a>
# `init`

<a id="init-init"></a>
## `init.init`

```python
def init(root_path: Path | str, safety: bool) -> None:
```

Initialize a new markupdown project by copying the example directory structure.

**Args:**

- `root_path`: The target directory where the example should be copied.
Defaults to current directory.
- `safety`: Confirms if the target directory is not empty before initializing.
Defaults to True.



<a id="link"></a>
# `link`

<a id="link-link"></a>
## `link.link`

```python
def link(glob_pattern: str) -> None:
```

Sets the 'link' field in frontmatter for markdown files matching the glob pattern.

The link is constructed from the file path, with special handling for index.md files.
The path will be a relative path from the base directory of the glob pattern.

**Args:**

- `glob_pattern`: The glob pattern to match markdown files to update.



<a id="ls"></a>
# `ls`

<a id="ls-ls"></a>
## `ls.ls`

```python
def ls(glob_pattern: str) -> tuple[Path, list[Path]]:
```

List files matching a glob pattern.

**Args:**

- `glob_pattern`: Relative or absolute glob pattern to match files.

**Returns:** A tuple containing (base_dir, list_of_matching_subpaths).



<a id="minify"></a>
# `minify`

<a id="minify-minify"></a>
## `minify.minify`

```python
def minify(glob_pattern: str) -> None:
```

Minify HTML, CSS, and JS files matching a glob pattern.

**Args:**

- `glob_pattern`: The glob pattern to match HTML, CSS, and JS files to minify.



<a id="pydoc"></a>
# `pydoc`

generate_docs.py

This script crawls a Python package directory, extracts docstrings from modules,
classes, functions, and methods using the `ast` module, and writes the results
to a single Markdown file.

Additional features:
  - Module names are shown as dotted names (e.g. "foo.bar.baz") rather than file paths.
  - For each __init__.py, if an __all__ is defined, an Exports section is generated.
  - The Table of Contents lists fully qualified names (e.g. foo.bar.MyClass.my_method) without prefixes.
  - Headers have descriptive HTML anchors derived from their dotted names.
  - For each function/method, its signature is included with type hints (if present) and its return type.
  - Autodetects docstring formats (Google-style, NumPy-style, etc.) and reformats them into Markdown.
  - The Exports section builds links to the documented sections by matching the actual headers.


<a id="pydoc-make-anchor"></a>
## `pydoc.make_anchor`

```python
def make_anchor(text):
```

Create a slug for the anchor by removing formatting,

lower-casing, and replacing non-alphanumeric characters with hyphens.


<a id="pydoc-add-header"></a>
## `pydoc.add_header`

```python
def add_header(header_text, level):
```

Create a markdown header with a unique, descriptive anchor and record it for the TOC.

**Args:**

- `header_text` (*str*): The header text (expected to be a fully qualified dotted name).
- `level` (*int*): The markdown header level (1 for h1, 2 for h2, etc.)

**Returns:** list of str: Markdown lines for the header (including an HTML anchor).


<a id="pydoc-get-module-name"></a>
## `pydoc.get_module_name`

```python
def get_module_name(file_path, package_dir):
```

Convert a file path to a dotted module name relative to package_dir.

For example, if package_dir is '/path/to/src' and file_path is
'/path/to/src/foo/bar/baz.py', the returned module name is 'foo.bar.baz'.
For __init__.py, the "__init__" part is dropped.

**Args:**

- `file_path` (*str*): The absolute or relative file path.
- `package_dir` (*str*): The root package directory.

**Returns:** (*str*) The dotted module name.


<a id="pydoc-extract-all-from-ast"></a>
## `pydoc.extract_all_from_ast`

```python
def extract_all_from_ast(tree):
```

Look for an assignment to __all__ in the module AST and extract its value.

**Args:**

- `tree` (*ast.Module*): The parsed AST of the module.

**Returns:** list of str or None: The list of exported names if found, otherwise None.


<a id="pydoc-get-function-signature"></a>
## `pydoc.get_function_signature`

```python
def get_function_signature(node):
```

Build a string representation of the function/method signature,

including parameter type hints and the return type.

Note: Default values are not included.

**Args:**

- `node` (*ast.FunctionDef or ast.AsyncFunctionDef*): The function node.

**Returns:** (*str*) A signature string, e.g.:
def func(arg1: int, arg2: str, *args: Any, **kwargs: Any) -> bool:


<a id="pydoc-format-docstring"></a>
## `pydoc.format_docstring`

```python
def format_docstring(docstring):
```

Parse a docstring and reformat its components as Markdown.

**Args:**

- `docstring` (*str*): The raw docstring.

**Returns:** (*str*) The formatted Markdown version of the docstring.


<a id="pydoc-extract-docstrings-from-node"></a>
## `pydoc.extract_docstrings_from_node`

```python
def extract_docstrings_from_node(node, parent_qualname, heading_level):
```

Recursively extract docstrings from an AST node using fully qualified dotted names.

For functions and methods, the signature (with type hints) is included.
Docstrings are parsed (as Google-style) and reformatted into Markdown.

**Args:**

- `node` (*ast.AST*): The AST node (e.g. Module, ClassDef, FunctionDef).
- `parent_qualname` (*str*): The fully qualified name of the parent (module or class).
- `heading_level` (*int*): The markdown header level to use.

**Returns:** list of str: Lines of markdown documenting the node.


<a id="pydoc-process-file"></a>
## `pydoc.process_file`

```python
def process_file(file_path, package_dir):
```

Process a single Python file to extract its documentation as markdown text.

If the file is an __init__.py, also extract its __all__.

**Args:**

- `file_path` (*str*): The path to the Python (.py) file.
- `package_dir` (*str*): The root package directory (used for computing module name).

**Returns:** (*str*) The markdown-formatted documentation extracted from the file.


<a id="pydoc-crawl-directory"></a>
## `pydoc.crawl_directory`

```python
def crawl_directory(directory):
```

Recursively crawl a directory, process each Python file, and concatenate

their markdown documentation.

**Args:**

- `directory` (*str*): The root directory to crawl.

**Returns:** (*str*) The combined markdown documentation for the entire package.


<a id="pydoc-generate-toc"></a>
## `pydoc.generate_toc`

```python
def generate_toc():
```

Generate a Markdown-formatted Table of Contents based on the collected headers.

**Returns:** list of str: Lines for the Table of Contents.


<a id="pydoc-generate-exports-section"></a>
## `pydoc.generate_exports_section`

```python
def generate_exports_section():
```

Generate a Markdown section listing __all__ exports for modules that define it.

Each module and export is linked to its respective section.

**Returns:** list of str: Lines for the Exports section.


<a id="pydoc-main"></a>
## `pydoc.main`

```python
def main():
```


<a id="references"></a>
# `references`

<a id="references-references"></a>
## `references.references`

```python
def references(glob_pattern: str, ast_pattern: str | None) -> None:
```


<a id="render"></a>
# `render`

<a id="render-markupdownrenderer"></a>
## `render.MarkupdownRenderer`

<a id="render-markupdownrenderer-init"></a>
### `render.MarkupdownRenderer.__init__`

```python
def __init__(self, md_file: MarkdownFile, base_dir: Path | str, **kwargs):
```

<a id="render-markupdownrenderer-link"></a>
### `render.MarkupdownRenderer.link`

```python
def link(self, text, url, title):
```

<a id="render-markupdownrenderer-block-code"></a>
### `render.MarkupdownRenderer.block_code`

```python
def block_code(self, code, info):
```

<a id="render-render"></a>
## `render.render`

```python
def render(glob_pattern: str, site: dict[str, object], dest_dir: Path | str | None, template_dir: str | Path) -> None:
```

Render markdown files to HTML using liquid templates.

For each markdown file:
- Convert markdown content to HTML
- Apply liquid template specified in frontmatter (or default.liquid)
- Write rendered HTML to the same location with .html extension

**Args:**

- `glob_pattern`: The glob pattern of the markdown files to render.
- `site`: Dictionary of site configuration. Defaults to {}.
- `dest_dir`: Directory to render to.
Defaults to the base directory of the glob pattern.
- `template_dir`: Directory containing liquid templates.
Defaults to "templates" in current directory.

**Raises:**

- `FileNotFoundError` (*FileNotFoundError*): If template directory doesn't exist
- `ValueError` (*ValueError*): If no template is specified and no default.liquid exists



<a id="serve"></a>
# `serve`

<a id="serve-serve"></a>
## `serve.serve`

```python
def serve(port: int, build_script: Path | str, site_dir: Path | str, watch_dirs: list[Path | str]):
```

Start a local development server to preview the generated site.

Uses the build.py script to rebuild the site when changes are detected.

**Args:**

- `port`: The port number to run the server on. Defaults to 8000.
- `build_script`: The build.py script to use. Defaults to "build.py".
- `site_dir`: The directory to serve. Defaults to "site".
- `watch_dirs`: Directories to watch for changes.
Defaults to ["content", "templates", "assets", "build.py"].



<a id="siblings"></a>
# `siblings`

<a id="siblings-siblings"></a>
## `siblings.siblings`

```python
def siblings(glob_pattern: str) -> None:
```


<a id="sitemap"></a>
# `sitemap`

<a id="sitemap-sitemap"></a>
## `sitemap.sitemap`

```python
def sitemap(glob_pattern: str, site_url: str, dest_dir: Path | str | None, default_priority: float, default_changefreq: str) -> None:
```

Generate a sitemap.xml from markdown files matching a glob pattern.

**Args:**

- `glob_pattern`: The glob pattern to match markdown files to include in the sitemap.
- `site_url`: Base URL of the website (e.g., 'https://example.com').
- `dest_dir`: Directory to write the sitemap to.
Defaults to the base directory of the glob pattern.
- `default_priority`: Default priority for URLs (0.0 to 1.0).
- `default_changefreq`: Default change frequency.
Options: always, hourly, daily, weekly, monthly, yearly, never.



<a id="title"></a>
# `title`

<a id="title-title"></a>
## `title.title`

```python
def title(glob_pattern: str, ast_pattern: str | None) -> None:
```

Sets titles for markdown files that don't have a `title` field in their frontmatter.

Uses the first # h1 as the title if ast_pattern is not provided. If no # h1 is found,
the filename is used with the following rules:

- Replace .md with empty string
- Replace - with spaces
- Capitalize

**Args:**

- `glob_pattern`: The glob pattern of the markdown files to update.
- `ast_pattern`: The jmespath expression to select the title.
Defaults to the first # h1.



<a id="transform"></a>
# `transform`

<a id="transform-transform"></a>
## `transform.transform`

```python
def transform(glob_pattern: str, func: Callable[[MarkdownFile, Path], Any]) -> None:
```

Apply a transformation function to markdown files matching a glob pattern.

**Args:**

- `glob_pattern`: The glob pattern to match markdown files to transform.
- `func`: A callable that takes a MarkdownFile and SiteFile as arguments and applies
the desired transformation.



<a id="util"></a>
# `util`

<a id="util-init-logger"></a>
## `util.init_logger`

```python
def init_logger() -> None:
```

<a id="util-resolve-base"></a>
## `util.resolve_base`

```python
def resolve_base(glob_pattern: str) -> tuple[Path, str]:
```

Given a glob pattern, resolve the base directory and relative glob pattern.

Some examples:

- "site/**/*.md" -> ("site", "**/*.md")
- "**/*.md" -> (current directory, "**/*.md")
- "post[s]/index.md" -> (current directory, "post[s]/index.md")
- "/pages/post[s]/index.md" -> ("/pages", "post[s]/index.md")


<a id="util-htmlstripper"></a>
## `util.HTMLStripper`

<a id="util-htmlstripper-init"></a>
### `util.HTMLStripper.__init__`

```python
def __init__(self):
```

<a id="util-htmlstripper-handle-data"></a>
### `util.HTMLStripper.handle_data`

```python
def handle_data(self, data: str):
```

<a id="util-htmlstripper-get-data"></a>
### `util.HTMLStripper.get_data`

```python
def get_data(self):
```

<a id="util-strip-html"></a>
## `util.strip_html`

```python
def strip_html(html: str) -> str:
```

