#!/usr/bin/env python3
"""
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
"""

import ast
import os
import re
import argparse
import docstring_parser  # Requires: pip install docstring-parser

# Global variables for the Table of Contents, anchors, and export info
toc_entries = []       # List of tuples: (level, header_text, anchor)
anchor_usage = {}      # To ensure unique anchors based on header text
exports_by_module = {} # Mapping: module_name -> list of exported names (from __all__)


def make_anchor(text):
    """
    Create a slug for the anchor by removing formatting,
    lower-casing, and replacing non-alphanumeric characters with hyphens.
    """
    text = text.replace("`", "").lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')


def add_header(header_text, level):
    """
    Create a markdown header with a unique, descriptive anchor and record it for the TOC.

    Args:
        header_text (str): The header text (expected to be a fully qualified dotted name).
        level (int): The markdown header level (1 for h1, 2 for h2, etc.)

    Returns:
        list of str: Markdown lines for the header (including an HTML anchor).
    """
    global anchor_usage, toc_entries

    anchor_base = make_anchor(header_text)
    count = anchor_usage.get(anchor_base, 0)
    if count:
        anchor = f"{anchor_base}-{count+1}"
    else:
        anchor = anchor_base
    anchor_usage[anchor_base] = count + 1

    toc_entries.append((level, header_text, anchor))
    return [f'<a id="{anchor}"></a>', f'{"#" * level} `{header_text}`']


def get_module_name(file_path, package_dir):
    """
    Convert a file path to a dotted module name relative to package_dir.
    
    For example, if package_dir is '/path/to/src' and file_path is
    '/path/to/src/foo/bar/baz.py', the returned module name is 'foo.bar.baz'.
    For __init__.py, the "__init__" part is dropped.
    
    Args:
        file_path (str): The absolute or relative file path.
        package_dir (str): The root package directory.
    
    Returns:
        str: The dotted module name.
    """
    rel_path = os.path.relpath(file_path, package_dir)
    if rel_path.endswith('.py'):
        rel_path = rel_path[:-3]  # remove ".py"
    parts = rel_path.split(os.sep)
    if parts[-1] == '__init__':
        parts = parts[:-1]
    if not parts:
        return os.path.basename(os.path.abspath(package_dir))
    return ".".join(parts)


def extract_all_from_ast(tree):
    """
    Look for an assignment to __all__ in the module AST and extract its value.

    Args:
        tree (ast.Module): The parsed AST of the module.

    Returns:
        list of str or None: The list of exported names if found, otherwise None.
    """
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__":
                    if isinstance(node.value, (ast.List, ast.Tuple)):
                        items = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Str):
                                items.append(elt.s)
                            elif hasattr(ast, "Constant") and isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                                items.append(elt.value)
                        return items
    return None


def get_function_signature(node):
    """
    Build a string representation of the function/method signature,
    including parameter type hints and the return type.
    
    Note: Default values are not included.
    
    Args:
        node (ast.FunctionDef or ast.AsyncFunctionDef): The function node.
    
    Returns:
        str: A signature string, e.g.:
             def func(arg1: int, arg2: str, *args: Any, **kwargs: Any) -> bool:
    """
    args_list = []
    posonly = getattr(node.args, "posonlyargs", [])
    for arg in posonly:
        if arg.annotation is not None:
            annotation_str = ast.unparse(arg.annotation)
            args_list.append(f"{arg.arg}: {annotation_str}")
        else:
            args_list.append(arg.arg)
    if posonly:
        args_list.append("/")
    for arg in node.args.args:
        if arg.annotation is not None:
            annotation_str = ast.unparse(arg.annotation)
            args_list.append(f"{arg.arg}: {annotation_str}")
        else:
            args_list.append(arg.arg)
    if node.args.vararg:
        vararg = node.args.vararg
        if vararg.annotation is not None:
            annotation_str = ast.unparse(vararg.annotation)
            args_list.append(f"*{vararg.arg}: {annotation_str}")
        else:
            args_list.append("*" + vararg.arg)
    elif node.args.kwonlyargs:
        args_list.append("*")
    for arg in node.args.kwonlyargs:
        if arg.annotation is not None:
            annotation_str = ast.unparse(arg.annotation)
            args_list.append(f"{arg.arg}: {annotation_str}")
        else:
            args_list.append(arg.arg)
    if node.args.kwarg:
        kwarg = node.args.kwarg
        if kwarg.annotation is not None:
            annotation_str = ast.unparse(kwarg.annotation)
            args_list.append(f"**{kwarg.arg}: {annotation_str}")
        else:
            args_list.append("**" + kwarg.arg)
    signature = f"def {node.name}({', '.join(args_list)})"
    if node.returns is not None:
        return_type_str = ast.unparse(node.returns)
        signature += f" -> {return_type_str}"
    signature += ":"
    return signature


def format_docstring(docstring):
    """
    Parse a docstring and reformat its components as Markdown.
    
    Args:
        docstring (str): The raw docstring.
    
    Returns:
        str: The formatted Markdown version of the docstring.
    """
    try:
        parsed = docstring_parser.parse(docstring, style=docstring_parser.DocstringStyle.AUTO)
    except Exception as e:
        # If parsing fails, return the original docstring.
        return docstring

    lines = []
    if parsed.short_description:
        lines.append(parsed.short_description)
        lines.append("")
    if parsed.long_description:
        lines.append(parsed.long_description)
        lines.append("")
    if parsed.params:
        lines.append("**Args:**")
        lines.append("")
        for param in parsed.params:
            type_part = f" (*{param.type_name}*)" if param.type_name else ""
            lines.append(f"- `{param.arg_name}`{type_part}: {param.description}")
        lines.append("")
    if parsed.returns:
        type_part = f" (*{parsed.returns.type_name}*)" if parsed.returns.type_name else ""
        lines.append(f"**Returns:**{type_part} {parsed.returns.description}")
        lines.append("")
    if parsed.raises:
        lines.append("**Raises:**")
        lines.append("")
        for exc in parsed.raises:
            type_part = f" (*{exc.type_name}*)" if exc.type_name else ""
            lines.append(f"- `{exc.type_name}`{type_part}: {exc.description}")
        lines.append("")
    return "\n".join(lines)


def extract_docstrings_from_node(node, parent_qualname, heading_level=2):
    """
    Recursively extract docstrings from an AST node using fully qualified dotted names.
    For functions and methods, the signature (with type hints) is included.
    Docstrings are parsed (as Google-style) and reformatted into Markdown.

    Args:
        node (ast.AST): The AST node (e.g. Module, ClassDef, FunctionDef).
        parent_qualname (str): The fully qualified name of the parent (module or class).
        heading_level (int): The markdown header level to use.

    Returns:
        list of str: Lines of markdown documenting the node.
    """
    lines = []

    if isinstance(node, ast.Module):
        module_doc = ast.get_docstring(node)
        if module_doc:
            lines.append(format_docstring(module_doc))
            lines.append("")
        for child in node.body:
            lines.extend(extract_docstrings_from_node(child, parent_qualname, heading_level))
        return lines

    if isinstance(node, ast.ClassDef):
        qname = f"{parent_qualname}.{node.name}" if parent_qualname else node.name
        lines.extend(add_header(qname, level=heading_level))
        lines.append("")
        class_doc = ast.get_docstring(node)
        if class_doc:
            lines.append(format_docstring(class_doc))
            lines.append("")
        for child in node.body:
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                lines.extend(extract_docstrings_from_node(child, qname, heading_level + 1))
        return lines

    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        qname = f"{parent_qualname}.{node.name}" if parent_qualname else node.name
        lines.extend(add_header(qname, level=heading_level))
        lines.append("")
        signature = get_function_signature(node)
        lines.append("```python")
        lines.append(signature)
        lines.append("```")
        lines.append("")
        func_doc = ast.get_docstring(node)
        if func_doc:
            lines.append(format_docstring(func_doc))
            lines.append("")
        return lines

    return lines


def process_file(file_path, package_dir):
    """
    Process a single Python file to extract its documentation as markdown text.
    If the file is an __init__.py, also extract its __all__.

    Args:
        file_path (str): The path to the Python (.py) file.
        package_dir (str): The root package directory (used for computing module name).

    Returns:
        str: The markdown-formatted documentation extracted from the file.
    """
    try:
        with open(file_path, "r", encoding="utf8") as f:
            source = f.read()
        tree = ast.parse(source, filename=file_path)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return ""

    module_name = get_module_name(file_path, package_dir)
    md_lines = []
    md_lines.extend(add_header(module_name, level=1))
    md_lines.append("")

    if os.path.basename(file_path) == "__init__.py":
        exported = extract_all_from_ast(tree)
        if exported is not None:
            exports_by_module[module_name] = exported

    md_lines.extend(extract_docstrings_from_node(tree, parent_qualname=module_name, heading_level=2))
    md_lines.append("")
    return "\n".join(md_lines)


def crawl_directory(directory):
    """
    Recursively crawl a directory, process each Python file, and concatenate
    their markdown documentation.

    Args:
        directory (str): The root directory to crawl.

    Returns:
        str: The combined markdown documentation for the entire package.
    """
    all_docs = []
    for root, _, files in os.walk(directory):
        for file in sorted(files):
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                file_docs = process_file(file_path, directory)
                if file_docs:
                    all_docs.append(file_docs)
    return "\n".join(all_docs)


def generate_toc():
    """
    Generate a Markdown-formatted Table of Contents based on the collected headers.

    Returns:
        list of str: Lines for the Table of Contents.
    """
    lines = []
    lines.append("## Table of Contents")
    lines.append("")
    for level, header_text, anchor in toc_entries:
        header_text = f"`{header_text}`"
        indent = "  " * (level - 1)
        lines.append(f"{indent}- [{header_text}](#{anchor})")
    lines.append("")
    return lines


def generate_exports_section():
    """
    Generate a Markdown section listing __all__ exports for modules that define it.
    Each module and export is linked to its respective section.
    
    Returns:
        list of str: Lines for the Exports section.
    """
    lines = []
    if exports_by_module:
        lines.append("## Exports")
        lines.append("")
        for module in sorted(exports_by_module.keys()):
            module_anchor = None
            for lvl, header_text, anchor in toc_entries:
                if header_text == module:
                    module_anchor = anchor
                    break
            if module_anchor is None:
                module_anchor = make_anchor(module)
            lines.append(f"- [`{module}`](#{module_anchor}):")
            for export in sorted(exports_by_module[module]):
                export_anchor = None
                for lvl, header_text, anchor in toc_entries:
                    if header_text == f"{module}.{export}" or header_text.endswith(f".{export}"):
                        export_anchor = anchor
                        break
                if export_anchor is None:
                    export_anchor = make_anchor(f"{module}.{export}")
                lines.append(f"  - [`{export}`](#{export_anchor})")
        lines.append("")
    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Generate a Markdown documentation file from a Python package directory."
    )
    parser.add_argument("package_dir", help="Path to the Python package directory")
    parser.add_argument("output_file", help="Path to the output Markdown file")
    args = parser.parse_args()

    docs_content = crawl_directory(args.package_dir)

    final_lines = []
    final_lines.append("# Documentation")
    final_lines.append("")
    final_lines.extend(generate_toc())
    final_lines.extend(generate_exports_section())
    final_lines.append(docs_content)
    final_content = "\n".join(final_lines)

    try:
        with open(args.output_file, "w", encoding="utf8") as f:
            f.write(final_content)
        print(f"Documentation successfully generated and saved to '{args.output_file}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")


if __name__ == "__main__":
    main()
