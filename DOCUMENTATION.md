# `markupdown`

## Table of Contents

- 🅼 [markupdown](#markupdown)
- 🅼 [markupdown\.\_\_main\_\_](#markupdown-__main__)
- 🅼 [markupdown\.blurb](#markupdown-blurb)
- 🅼 [markupdown\.changelog](#markupdown-changelog)
- 🅼 [markupdown\.children](#markupdown-children)
- 🅼 [markupdown\.clean](#markupdown-clean)
- 🅼 [markupdown\.cp](#markupdown-cp)
- 🅼 [markupdown\.feed](#markupdown-feed)
- 🅼 [markupdown\.files](#markupdown-files)
- 🅼 [markupdown\.init](#markupdown-init)
- 🅼 [markupdown\.link](#markupdown-link)
- 🅼 [markupdown\.ls](#markupdown-ls)
- 🅼 [markupdown\.minify](#markupdown-minify)
- 🅼 [markupdown\.references](#markupdown-references)
- 🅼 [markupdown\.render](#markupdown-render)
- 🅼 [markupdown\.serve](#markupdown-serve)
- 🅼 [markupdown\.siblings](#markupdown-siblings)
- 🅼 [markupdown\.sitemap](#markupdown-sitemap)
- 🅼 [markupdown\.title](#markupdown-title)
- 🅼 [markupdown\.toc](#markupdown-toc)
- 🅼 [markupdown\.transform](#markupdown-transform)
- 🅼 [markupdown\.util](#markupdown-util)

<a name="markupdown"></a>
## 🅼 markupdown

- **[Exports](#markupdown-exports)**

<a name="markupdown-exports"></a>
### Exports

- 🅼 [`blurb`](#markupdown-blurb)
- 🅼 [`cp`](#markupdown-cp)
- 🅼 [`init`](#markupdown-init)
- 🅼 [`ls`](#markupdown-ls)
- 🅼 [`render`](#markupdown-render)
- 🅼 [`serve`](#markupdown-serve)
- 🅼 [`title`](#markupdown-title)
- 🅼 [`link`](#markupdown-link)
- 🅼 [`clean`](#markupdown-clean)
- 🅼 [`changelog`](#markupdown-changelog)
- 🅼 [`transform`](#markupdown-transform)
- 🅼 [`children`](#markupdown-children)
- 🅼 [`siblings`](#markupdown-siblings)
- 🅼 [`feed`](#markupdown-feed)
- 🅼 [`sitemap`](#markupdown-sitemap)
- 🅼 [`references`](#markupdown-references)
- 🅼 [`minify`](#markupdown-minify)
- 🅼 [`toc`](#markupdown-toc)
<a name="markupdown-__main__"></a>
## 🅼 markupdown\.\_\_main\_\_
<a name="markupdown-blurb"></a>
## 🅼 markupdown\.blurb

- **Constants:**
  - 🆅 [FIRST\_PARAGRAPH\_RE](#markupdown-blurb-FIRST_PARAGRAPH_RE)
- **Functions:**
  - 🅵 [blurb](#markupdown-blurb-blurb)

### Constants

<a name="markupdown-blurb-FIRST_PARAGRAPH_RE"></a>
### 🆅 markupdown\.blurb\.FIRST\_PARAGRAPH\_RE

```python
FIRST_PARAGRAPH_RE = re.compile('(?s)(?:\\A|\\n\\n)(?![ \\t]*(?:#{1,6}\\s|>|\\* |- |\\+ |\\d+\\.\\s))(.+?)(?=\\n\\n|\\Z)')
```

### Functions

<a name="markupdown-blurb-blurb"></a>
### 🅵 markupdown\.blurb\.blurb

```python
def blurb(glob_pattern: str, max_length: int = 200) -> None:
```

Sets blurb for markdown files that don't have a \`blurb\` field in their frontmatter\.

Uses the first non-heading paragraph as the blurb if ast\_pattern is not provided\.
<a name="markupdown-changelog"></a>
## 🅼 markupdown\.changelog

- **Functions:**
  - 🅵 [changelog](#markupdown-changelog-changelog)

### Functions

<a name="markupdown-changelog-changelog"></a>
### 🅵 markupdown\.changelog\.changelog

```python
def changelog(glob_pattern: str = '**/*.md', dest_dir: Path | str | None = None) -> None:
```

Add git metadata to markdown frontmatter in files matching a glob pattern\. Adds:

- created\_at
    - updated\_at
    - changelog

The changelog field is a list of dictionaries with the following keys:

    - hash: The commit hash
    - author: The commit author
    - date: The commit date
    - message: The commit message

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to update\.
- **dest_dir**: Base directory of markdown files that should be updated\.
Not necessarily the same as the base directory of the glob pattern since
you might wish to get changelogs from source files in a git managed
content directory and apply them to a site directory that isn't in git\.
<a name="markupdown-children"></a>
## 🅼 markupdown\.children

- **Functions:**
  - 🅵 [children](#markupdown-children-children)

### Functions

<a name="markupdown-children-children"></a>
### 🅵 markupdown\.children\.children

```python
def children(glob_pattern: str) -> None:
```
<a name="markupdown-clean"></a>
## 🅼 markupdown\.clean

- **Functions:**
  - 🅵 [clean](#markupdown-clean-clean)

### Functions

<a name="markupdown-clean-clean"></a>
### 🅵 markupdown\.clean\.clean

```python
def clean(dir: Path | str | None = None, safety: bool = True):
```

Delete the contents of a directory if it exists\.

**Parameters:**

- **dir** (default: `the current directory`): The directory to clean\. Defaults to the current directory\.
- **safety**: Confirms if the directory to clean is not under the current directory\.
Defaults to True\.
<a name="markupdown-cp"></a>
## 🅼 markupdown\.cp

- **Functions:**
  - 🅵 [cp](#markupdown-cp-cp)

### Functions

<a name="markupdown-cp-cp"></a>
### 🅵 markupdown\.cp\.cp

```python
def cp(glob_pattern: str, dest_dir: Path | str) -> None:
```

Copy files matching a glob pattern to a destination directory\. If the file is a markdown

file, a \`source\` field will be added to the frontmatter in the copied file\.

**Parameters:**

- **glob_pattern**: The glob pattern to match files to copy\.
- **dest_dir**: The destination directory to copy files to\.
<a name="markupdown-feed"></a>
## 🅼 markupdown\.feed

- **Functions:**
  - 🅵 [feed](#markupdown-feed-feed)

### Functions

<a name="markupdown-feed-feed"></a>
### 🅵 markupdown\.feed\.feed

```python
def feed(glob_pattern: str, feed_id: str, feed_title: str, feed_link: str, feed_description: str, feed_author: str | None = None, dest_dir: Path | str | None = None) -> None:
```

Generate an RSS feed from markdown files matching a glob pattern\.

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to include in the feed\.
- **dest_dir**: Directory to write the RSS feed to\.
Defaults to the base directory of the glob pattern\.
- **feed_title** (default: `"Blog Feed"`): Title of the RSS feed\. Defaults to "Blog Feed"\.
- **feed_link** (default: `"http://example.com"`): Link to the website\. Defaults to "http://example\.com"\.
- **feed_description** (default: `"Latest blog posts"`): Description of the feed\. Defaults to "Latest blog posts"\.
<a name="markupdown-files"></a>
## 🅼 markupdown\.files

- **Constants:**
  - 🆅 [AST\_RENDERER](#markupdown-files-AST_RENDERER)
- **Classes:**
  - 🅲 [MarkdownFile](#markupdown-files-MarkdownFile)

### Constants

<a name="markupdown-files-AST_RENDERER"></a>
### 🆅 markupdown\.files\.AST\_RENDERER

```python
AST_RENDERER = mistune.create_markdown(renderer=None)
```

### Classes

<a name="markupdown-files-MarkdownFile"></a>
### 🅲 markupdown\.files\.MarkdownFile

```python
class MarkdownFile:
```

**Functions:**

<a name="markupdown-files-MarkdownFile-__init__"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.\_\_init\_\_

```python
def __init__(self, path: Path | str) -> None:
```
<a name="markupdown-files-MarkdownFile-frontmatter"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.frontmatter

```python
def frontmatter(self) -> dict[str, object]:
```
<a name="markupdown-files-MarkdownFile-content"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.content

```python
def content(self) -> str:
```
<a name="markupdown-files-MarkdownFile-ast"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.ast

```python
def ast(self) -> list[dict[str, object]]:
```
<a name="markupdown-files-MarkdownFile-set_content"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.set\_content

```python
def set_content(self, content: str) -> None:
```
<a name="markupdown-files-MarkdownFile-update_frontmatter"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.update\_frontmatter

```python
def update_frontmatter(self, metadata: dict[str, object]) -> None:
```
<a name="markupdown-files-MarkdownFile-del_frontmatter_key"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.del\_frontmatter\_key

```python
def del_frontmatter_key(self, key: str) -> None:
```
<a name="markupdown-files-MarkdownFile-url_path"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.url\_path

```python
def url_path(self, base_dir: Path | str) -> str:
```

Returns the URL path of the current page relative to the base directory\.

For example, if we have:

- self\.path: /home/alice/blog/posts/this-post\.md
- base\_dir: /home/alice/blog

The returned URL is /posts/this-post

**Parameters:**

- **base_dir**: The base directory to resolve the link against\.

**Returns:**

- The URL of the current page relative to the base directory\.
<a name="markupdown-files-MarkdownFile-resolve"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.resolve

```python
def resolve(self, base_dir: Path | str, rel_path: Path | str) -> Path:
```

Converts a path relative to the current markdown file into a subpath

relative to the base directory\. For example, if we have:

- self\.path: /home/alice/blog/posts/this-post\.md
- base\_dir: /home/alice/blog
- rel\_path: \.\./index\.md

The returned path is index\.md

**Parameters:**

- **base_dir**: The base directory to resolve the link against\.
- **rel_path**: The relative path to resolve\.

**Returns:**

- The absolute path of the relative path\.
<a name="markupdown-files-MarkdownFile-subpath"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.subpath

```python
def subpath(self, base_dir: Path | str) -> Path:
```

Returns the path of the current page relative to the base directory\.

For example, if we have:

- self\.path: /home/alice/blog/posts/this-post\.md
- base\_dir: /home/alice/blog

The returned path is posts/this-post\.md

**Parameters:**

- **base_dir**: The base directory to resolve the link against\.

**Returns:**

- The path of the current page relative to the base directory\.
<a name="markupdown-files-MarkdownFile-save"></a>
#### 🅵 markupdown\.files\.MarkdownFile\.save

```python
def save(self) -> None:
```
<a name="markupdown-init"></a>
## 🅼 markupdown\.init

- **Functions:**
  - 🅵 [init](#markupdown-init-init)

### Functions

<a name="markupdown-init-init"></a>
### 🅵 markupdown\.init\.init

```python
def init(root_path: Path | str = '.', safety: bool = True) -> None:
```

Initialize a new markupdown project by copying the example directory structure\.

**Parameters:**

- **root_path**: The target directory where the example should be copied\.
Defaults to current directory\.
- **safety**: Confirms if the target directory is not empty before initializing\.
Defaults to True\.
<a name="markupdown-link"></a>
## 🅼 markupdown\.link

- **Functions:**
  - 🅵 [link](#markupdown-link-link)

### Functions

<a name="markupdown-link-link"></a>
### 🅵 markupdown\.link\.link

```python
def link(glob_pattern: str) -> None:
```

Sets the 'link' field in frontmatter for markdown files matching the glob pattern\.

The link is constructed from the file path, with special handling for index\.md files\.
The path will be a relative path from the base directory of the glob pattern\.

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to update\.
<a name="markupdown-ls"></a>
## 🅼 markupdown\.ls

- **Functions:**
  - 🅵 [ls](#markupdown-ls-ls)

### Functions

<a name="markupdown-ls-ls"></a>
### 🅵 markupdown\.ls\.ls

```python
def ls(glob_pattern: str) -> tuple[Path, list[Path]]:
```

List files matching a glob pattern\.

**Parameters:**

- **glob_pattern**: Relative or absolute glob pattern to match files\.

**Returns:**

- A tuple containing \(base\_dir, list\_of\_matching\_subpaths\)\.
<a name="markupdown-minify"></a>
## 🅼 markupdown\.minify

- **Functions:**
  - 🅵 [minify](#markupdown-minify-minify)

### Functions

<a name="markupdown-minify-minify"></a>
### 🅵 markupdown\.minify\.minify

```python
def minify(glob_pattern: str) -> None:
```

Minify HTML, CSS, and JS files matching a glob pattern\.

**Parameters:**

- **glob_pattern**: The glob pattern to match HTML, CSS, and JS files to minify\.
<a name="markupdown-references"></a>
## 🅼 markupdown\.references

- **Constants:**
  - 🆅 [A\_HREF\_AST\_PATH](#markupdown-references-A_HREF_AST_PATH)
- **Functions:**
  - 🅵 [references](#markupdown-references-references)

### Constants

<a name="markupdown-references-A_HREF_AST_PATH"></a>
### 🆅 markupdown\.references\.A\_HREF\_AST\_PATH

```python
A_HREF_AST_PATH = '$..attrs.url'
```

### Functions

<a name="markupdown-references-references"></a>
### 🅵 markupdown\.references\.references

```python
def references(glob_pattern: str, ast_pattern: str | None = None) -> None:
```
<a name="markupdown-render"></a>
## 🅼 markupdown\.render

- **Functions:**
  - 🅵 [render](#markupdown-render-render)
- **Classes:**
  - 🅲 [MarkupdownRenderer](#markupdown-render-MarkupdownRenderer)
  - 🅲 [TocHeadingGenerator](#markupdown-render-TocHeadingGenerator)

### Functions

<a name="markupdown-render-render"></a>
### 🅵 markupdown\.render\.render

```python
def render(glob_pattern: str, site: dict[str, object] = {}, dest_dir: Path | str | None = None, template_dir: str | Path = 'templates') -> None:
```

Render markdown files to HTML using liquid templates\.

For each markdown file:
- Convert markdown content to HTML
- Apply liquid template specified in frontmatter \(or default\.liquid\)
- Write rendered HTML to the same location with \.html extension

**Parameters:**

- **glob_pattern**: The glob pattern of the markdown files to render\.
- **site** (default: `{}`): Dictionary of site configuration\. Defaults to \{\}\.
- **dest_dir**: Directory to render to\.
Defaults to the base directory of the glob pattern\.
- **template_dir**: Directory containing liquid templates\.
Defaults to "templates" in current directory\.

**Raises:**

- **FileNotFoundError**: If template directory doesn't exist
- **ValueError**: If no template is specified and no default\.liquid exists

### Classes

<a name="markupdown-render-MarkupdownRenderer"></a>
### 🅲 markupdown\.render\.MarkupdownRenderer

```python
class MarkupdownRenderer(mistune.HTMLRenderer):
```

**Functions:**

<a name="markupdown-render-MarkupdownRenderer-__init__"></a>
#### 🅵 markupdown\.render\.MarkupdownRenderer\.\_\_init\_\_

```python
def __init__(self, md_file: MarkdownFile, base_dir: Path | str, **kwargs):
```
<a name="markupdown-render-MarkupdownRenderer-link"></a>
#### 🅵 markupdown\.render\.MarkupdownRenderer\.link

```python
def link(self, text, url, title = None):
```
<a name="markupdown-render-MarkupdownRenderer-block_code"></a>
#### 🅵 markupdown\.render\.MarkupdownRenderer\.block\_code

```python
def block_code(self, code, info = None):
```
<a name="markupdown-render-TocHeadingGenerator"></a>
### 🅲 markupdown\.render\.TocHeadingGenerator

```python
class TocHeadingGenerator:
```

**Functions:**

<a name="markupdown-render-TocHeadingGenerator-__init__"></a>
#### 🅵 markupdown\.render\.TocHeadingGenerator\.\_\_init\_\_

```python
def __init__(self) -> None:
```
<a name="markupdown-render-TocHeadingGenerator-__call__"></a>
#### 🅵 markupdown\.render\.TocHeadingGenerator\.\_\_call\_\_

```python
def __call__(self, token: dict[str, Any], _: int) -> str:
```
<a name="markupdown-serve"></a>
## 🅼 markupdown\.serve

- **Functions:**
  - 🅵 [serve](#markupdown-serve-serve)

### Functions

<a name="markupdown-serve-serve"></a>
### 🅵 markupdown\.serve\.serve

```python
def serve(port: int = 8000, build_script: Path | str = 'build.py', site_dir: Path | str = 'site', watch_dirs: list[Path | str] = []):
```

Start a local development server to preview the generated site\.

Uses the build\.py script to rebuild the site when changes are detected\.

**Parameters:**

- **port** (default: `8000`): The port number to run the server on\. Defaults to 8000\.
- **build_script** (default: `"build.py"`): The build\.py script to use\. Defaults to "build\.py"\.
- **site_dir** (default: `"site"`): The directory to serve\. Defaults to "site"\.
- **watch_dirs**: Directories to watch for changes\.
Defaults to \["content", "templates", "assets", "build\.py"\]\.
<a name="markupdown-siblings"></a>
## 🅼 markupdown\.siblings

- **Functions:**
  - 🅵 [siblings](#markupdown-siblings-siblings)

### Functions

<a name="markupdown-siblings-siblings"></a>
### 🅵 markupdown\.siblings\.siblings

```python
def siblings(glob_pattern: str) -> None:
```
<a name="markupdown-sitemap"></a>
## 🅼 markupdown\.sitemap

- **Functions:**
  - 🅵 [sitemap](#markupdown-sitemap-sitemap)

### Functions

<a name="markupdown-sitemap-sitemap"></a>
### 🅵 markupdown\.sitemap\.sitemap

```python
def sitemap(glob_pattern: str, site_url: str, dest_dir: Path | str | None = None, default_priority: float = 0.5, default_changefreq: str = 'weekly') -> None:
```

Generate a sitemap\.xml from markdown files matching a glob pattern\.

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to include in the sitemap\.
- **site_url**: Base URL of the website \(e\.g\., 'https://example\.com'\)\.
- **dest_dir**: Directory to write the sitemap to\.
Defaults to the base directory of the glob pattern\.
- **default_priority**: Default priority for URLs \(0\.0 to 1\.0\)\.
- **default_changefreq**: Default change frequency\.
Options: always, hourly, daily, weekly, monthly, yearly, never\.
<a name="markupdown-title"></a>
## 🅼 markupdown\.title

- **Constants:**
  - 🆅 [PAGE\_TITLE\_AST\_PATH](#markupdown-title-PAGE_TITLE_AST_PATH)
- **Functions:**
  - 🅵 [title](#markupdown-title-title)

### Constants

<a name="markupdown-title-PAGE_TITLE_AST_PATH"></a>
### 🆅 markupdown\.title\.PAGE\_TITLE\_AST\_PATH

```python
PAGE_TITLE_AST_PATH = '$[?(@.type == "heading" & @.attrs.level == 1 & @.children[0].type == "text")].children[0].raw'
```

### Functions

<a name="markupdown-title-title"></a>
### 🅵 markupdown\.title\.title

```python
def title(glob_pattern: str, ast_pattern: str | None = None) -> None:
```

Sets titles for markdown files that don't have a \`title\` field in their frontmatter\.

Uses the first \# h1 as the title if ast\_pattern is not provided\. If no \# h1 is found,
the filename is used with the following rules:

- Replace \.md with empty string
- Replace - with spaces
- Capitalize

**Parameters:**

- **glob_pattern**: The glob pattern of the markdown files to update\.
- **ast_pattern**: The jmespath expression to select the title\.
Defaults to the first \# h1\.
<a name="markupdown-toc"></a>
## 🅼 markupdown\.toc

- **Functions:**
  - 🅵 [toc](#markupdown-toc-toc)

### Functions

<a name="markupdown-toc-toc"></a>
### 🅵 markupdown\.toc\.toc

```python
def toc(glob_pattern: str) -> None:
```

Sets the 'toc' field in frontmatter for markdown files matching the glob pattern\.

The 'toc' field is a list of dicts with the following keys:
    - 'level': The heading level
    - 'slug': The slug of the heading
    - 'title': The text of the heading

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to update\.
<a name="markupdown-transform"></a>
## 🅼 markupdown\.transform

- **Functions:**
  - 🅵 [transform](#markupdown-transform-transform)

### Functions

<a name="markupdown-transform-transform"></a>
### 🅵 markupdown\.transform\.transform

```python
def transform(glob_pattern: str, func: Callable[[MarkdownFile, Path], Any]) -> None:
```

Apply a transformation function to markdown files matching a glob pattern\.

**Parameters:**

- **glob_pattern**: The glob pattern to match markdown files to transform\.
- **func**: A callable that takes a MarkdownFile and SiteFile as arguments and applies
the desired transformation\.
<a name="markupdown-util"></a>
## 🅼 markupdown\.util

- **Constants:**
  - 🆅 [LOGGING\_CONFIG](#markupdown-util-LOGGING_CONFIG)
- **Functions:**
  - 🅵 [init\_logger](#markupdown-util-init_logger)
  - 🅵 [resolve\_base](#markupdown-util-resolve_base)
  - 🅵 [strip\_html](#markupdown-util-strip_html)
- **Classes:**
  - 🅲 [HTMLStripper](#markupdown-util-HTMLStripper)

### Constants

<a name="markupdown-util-LOGGING_CONFIG"></a>
### 🆅 markupdown\.util\.LOGGING\_CONFIG

```python
LOGGING_CONFIG = {'version': 1, 'disable_existing_loggers': False, 'formatters': {'simple': {'format': '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'}}, 'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'simple', 'level': 'INFO'}}, 'loggers': {'markupdown': {'handlers': ['console'], 'level': 'WARNING', 'propagate': False}}}
```

### Functions

<a name="markupdown-util-init_logger"></a>
### 🅵 markupdown\.util\.init\_logger

```python
def init_logger() -> None:
```
<a name="markupdown-util-resolve_base"></a>
### 🅵 markupdown\.util\.resolve\_base

```python
def resolve_base(glob_pattern: str) -> tuple[Path, str]:
```

Given a glob pattern, resolve the base directory and relative glob pattern\.

Some examples:

- "site/\*\*/\*\.md" -\> \("site", "\*\*/\*\.md"\)
- "\*\*/\*\.md" -\> \(current directory, "\*\*/\*\.md"\)
- "post\[s\]/index\.md" -\> \(current directory, "post\[s\]/index\.md"\)
- "/pages/post\[s\]/index\.md" -\> \("/pages", "post\[s\]/index\.md"\)
<a name="markupdown-util-strip_html"></a>
### 🅵 markupdown\.util\.strip\_html

```python
def strip_html(html: str) -> str:
```

### Classes

<a name="markupdown-util-HTMLStripper"></a>
### 🅲 markupdown\.util\.HTMLStripper

```python
class HTMLStripper(HTMLParser):
```

**Functions:**

<a name="markupdown-util-HTMLStripper-__init__"></a>
#### 🅵 markupdown\.util\.HTMLStripper\.\_\_init\_\_

```python
def __init__(self):
```
<a name="markupdown-util-HTMLStripper-handle_data"></a>
#### 🅵 markupdown\.util\.HTMLStripper\.handle\_data

```python
def handle_data(self, data: str):
```
<a name="markupdown-util-HTMLStripper-get_data"></a>
#### 🅵 markupdown\.util\.HTMLStripper\.get\_data

```python
def get_data(self):
```
