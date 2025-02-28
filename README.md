# Markupdown

Markupdown is a collection of functions that help you build static sites with [markdown](https://daringfireball.net/projects/markdown/).

Many static site generators are complex, rigid, and rely on plugins for extensibility. Markupdown is the opposite: it's dumb but programmable. It's kind of like a build system for static sites. A typical flow looks like this:

- Stage your `site` directory with markdown, CSS, Javascript, images, and so forth (using `cp`)
- Transform your files to add metadata to the frontmatter (using functions like `title`, `link`, `blurb`, and so on)
- Render the markdown with [Liquid](https://shopify.github.io/liquid/) templates (using `render`)

You can call Markdown's functions any way you like, but I recommend creating a little `build.py` file in your project root:

```python
#!/usr/bin/env python3
from markupdown import *

# Copy files to the site directory
cp("assets/**/*.*", "site")
cp("content/**/*.md", "site")

# Update markdown frontmatter
title("site/**/*.md")
link("site/**/*.md")
blurb("site/**/*.md")
siblings("site/**/index.md")
children("site/**/index.md")
changelog("content/**/*.md", "site")
sitemap("site/**/*.md", site_url="http://example.com")

# Render site
render("site/**/*.md", site={"title": "My Site"})

# Minify site HTML, CSS, and JS
minify("site/**/*.html")
minify("site/**/*.css")
minify("site/**/*.js")
```

## Functions

Markupdown ships with the following functions:

- `blurb`: Updates the `blurb` field in markdown frontmatter to include a brief summary
- `changelog`: Updates the `created_at`, `updated_at`, and `change_log` fields in markdown frontmatter
- `children`: Generates `children` frontmatter for child directories with index.md files
- `clean`: Deletes the `site` directory
- `cp`: Copies files to the site directory
- `feed`: Generates RSS and Atom feeds
- `init`: Initializes a directory with an example site
- `link`: Updates the `link` field in markdown frontmatter with the relative URL path
- `minify`: Minifies HTML, CSS, and JS
- `references`: Parses markdown for hrefs and generates `references` and `backreferences` frontmatter for markdown files
- `render`: Renders markdown using Liquid templates
- `serve`: Starts a local HTTP server with live reload to view the site
- `siblings`: Generates `siblings` frontmatter that contains paths for sibling markdown files
- `sitemap`: Generates an XML sitemap
- `title`: Updates the `title` field frontmatter with the value of the first # h1 or filename
- `toc`: Generates a table of contents from markdown files
- `transform`: Applies a transformation function to the frontmatter in markdown files

See [DOCUMENTATION.md](./DOCUMENTATION.md) for more information.

## Installation

```bash
pip install markupdown
```

Markupdown is compatible with Python 3.10 to 3.12

## Usage

After you install Markupdown, go to an empty directory and initialize it:

```bash
python -m markupdown init
```

This will create a scaffolding with files and directories like this:

```text
.
├── assets
│   ├── css
│   │   └── style.css
│   ├── images
│   └── js
├── content
│   ├── index.md
│   └── posts
│       ├── index.md
│       ├── post1.md
│       └── post2.md
├── templates
│   ├── _footer_.liquid
│   ├── _head_.liquid
│   ├── _header_.liquid
│   ├── _pages_.liquid
│   └── default.liquid
├── .gitignore
└── build.py
```

Run `./build.py` to generate your site. The output will be in the `site` directory.

Markupdown comes with a server you can start with:

```bash
python -m markupdown serve
```

Open [http://localhost:8000](http://localhost:8000). You should see your new site.

You can clean your `site` directory with:

```bash
python -m markupdown clean
```
