- tags: Adds `tags` frontmatter for hashtags in markdown
- lint: Checks all markdown files for syntax, grammar, readability, and style.
- related: Generates related content frontmatter
- redirect: Redirects to a page using meta redirect
- json: Generates posts in JSON format

- Docs, docs, docs (https://pdoc.dev, markdown docs in repo, blog post on cnr.sh)
- Tests
- Look at using webassets.readthedocs.io

- Generate foo.md as foo/index.html instead of foo.html
- If a local link points to a directory, add index.md to the path
- Add rss.xml and sitemap.xml to the template head if they're set
- Set `<meta name="date" content="{{ page.created_at }}">` if `created_at` is set
- Add a debug message if transform returns failures
- Disable safe rendering for markdown files
- Add MARKUPDOWN_DEBUG env var to enable debug logging
- Make `transform` work with a single file as the glob pattern
- Live reload isn't working on cnr.sh
