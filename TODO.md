- tags: Adds `tags` frontmatter for hashtags in markdown
- lint: Checks all markdown files for syntax, grammar, readability, and style.
- related: Generates related content frontmatter
- redirect: Redirects to a page using meta redirect
- json: Generates posts in JSON format

- Docs, docs, docs (https://pdoc.dev, markdown docs in repo, blog post on cnr.sh)
- Tests
- Look at using webassets.readthedocs.io

- If a local link points to a directory, add index.md to the path
- Set `<meta name="date" content="{{ page.created_at }}">` if `created_at` is set
- Add MARKUPDOWN_DEBUG env var to enable debug logging
- Make `transform` work with a single file as the glob pattern
