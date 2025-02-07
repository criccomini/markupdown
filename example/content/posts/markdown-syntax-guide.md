# Markdown Syntax Guide

This post demonstrates all the common features of Markdown syntax. Use this as a reference for writing your own Markdown documents.

## Headers

# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header

## Emphasis

*This text is italicized*
_This is also italicized_

**This text is bold**
__This is also bold__

***This text is bold and italicized***

~~This text is strikethrough~~

## Lists

### Unordered List
* Item 1
* Item 2
  * Subitem 2.1
  * Subitem 2.2
* Item 3

### Ordered List
1. First item
2. Second item
3. Third item
   1. Subitem 3.1
   2. Subitem 3.2

## Links

[Visit OpenAI](https://www.openai.com)
[Visit Google][google-link]

[google-link]: https://www.google.com

## Images

![Markdown Logo](images/demo.png)

## Blockquotes

> This is a blockquote
> It can span multiple lines
>
> It can also have multiple paragraphs

## Code

Inline code: `const greeting = 'Hello, World!';`

Code block:
```python
def hello_world():
    print('Hello, World!')
    return True
```

## Tables

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

## Horizontal Rule

---

## Task Lists

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

## Footnotes

Here's a sentence with a footnote[^1].

[^1]: This is the footnote.

## Escaping Characters

\*This text is not italicized\*

## Final Notes

This concludes our markdown syntax demonstration. You can use these elements to create well-formatted documents, blog posts, and documentation.
