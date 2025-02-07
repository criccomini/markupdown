# Markupdown

Markupdown is a dead-simple static site generator. You write a `build.py` file that calls Markupdown commands and run it. Here's what a `build.py` file looks like:

```python
#!/usr/bin/env python3

from markupdown import *

# Copy files to the site directory
cp("assets/css/*.css", "site/css")
cp("assets/js/*.js", "site/js")
cp("assets/images/*.[jpg|jpeg|png]", "site/images")
cp("*.ico", "site")
cp("pages/**/*.md", "site")

# Update markdown frontmatter
title("site/**/*.md")
siblings("site/**/index.md")
children("site/**/index.md")
changelog("site/**/*.md")
transform("site/**/*.md", lambda md, _: md.frontmatter().pop("source", None))

# Render pages
render("site/**/*.md", site={"title": "My Site"})
```

Commands like `title` and `index` just scan a directory to create, update, or delete markdown files. `title`, for example, adds a `title` field to each matching markdown file's [frontmatter](https://jekyllrb.com/docs/front-matter/).

## Commands

Markupdown ships with the following commands:

- `changelog`: Updates the `created_at`, `updated_at`, and `change_log` fields in markdown frontmatter
- `cp`: Copies files to the site directory
- `transform`: Applies a transformation function to the frontmatter in markdown files
- `siblings`: Generates `siblings` frontmatter for sibling markdown files
- `children`: Generates `children` frontmatter for child directories with index.md files
- `init`: Initializes a new site
- `ls`: Lists files in the site directory
- `render`: Renders the markdown using [liquid](https://shopify.github.io/liquid/) templates
- `serve`: Starts a local HTTP server to view the site
- `title`: Updates the `title` field in the markdown frontmatter
- `feed`: Generates an RSS and Atom feeds

I'll probably add more (e.g. `sitemap`, `minify`, `social`). It's a work in progress.

## Installation

```bash
pip install markupdown
```

## Usage

After you install Markupdown, go to an empty directory and initialize it:

```bash
python -m markupdown init
```

This will create a scaffolding with files and directories like this:

```text
.
├── css
│   └── style.css
├── img
│   └── image.png
├── pages
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

Open [http://localhost:8000](http://localhost:8000). You should see a (rather ugly) stub site.

You can clean your `site` directory with:

```bash
python -m markupdown clean
```

## Philosophy

Markupdown is designed to be pretty dumb. It's just a collection of functions that help you do three things:

- Stage your `site` directory with markdown, css, js, images, and so forth (using `cp`)
- Transform the files in `site` to add metadata or create new files (using `title`, `index`, `nav`, etc.)
- Render the markdown using liquid templates (using `render`)

That's it. Stupid simple. Worse is better.
