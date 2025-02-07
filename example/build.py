#!/usr/bin/env python3

from markupdown import *

# Copy files to the site directory
cp("assets/css/*.css", "site/css")
cp("assets/js/*.js", "site/js")
cp("assets/images/*.png", "site/images")
cp("assets/*.ico", "site")
cp("content/**/*.md", "site")

# Update markdown frontmatter
title("site/**/*.md")
link("site/**/*.md")
blurb("site/**/*.md")
siblings("site/**/index.md")
children("site/**/index.md")
changelog("content/**/*.md", "site")
references("site/**/*.md")
feed(
    "site/**/*.md",
    feed_id="http://example.com",
    feed_title="My Site",
    feed_link="http://example.com",
    feed_description="My blog posts",
)
sitemap("site/**/*.md", site_url="http://example.com")

# Render site
render("site/**/*.md", site={"title": "My Site"})

# Minify site HTML, CSS, and JS
minify("site/**/*.html")
minify("site/**/*.css")
minify("site/**/*.js")