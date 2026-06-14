#!/usr/bin/env python3
"""Update the <header> and <footer> of every page from shared partials.

Reads `header.html` and `footer.html` at the site root and injects their
content into the matching <header class="site-header">...</header> and
<footer class="site-footer">...</footer> block of every other .html file.

The correct nav link is marked as active automatically, based on the file name.

Usage:
    python3 scripts/update_partials.py
"""

import re
import sys
from pathlib import Path

# Site root is the parent of the directory that holds this script.
ROOT = Path(__file__).resolve().parent.parent

# Partial files and the regex that locates the block they replace.
PARTIALS = {
    "header.html": re.compile(r'<header\b.*?</header>', re.DOTALL),
    "footer.html": re.compile(r'<footer\b.*?</footer>', re.DOTALL),
}

# Files that are partials/templates, not full pages to update.
SKIP = set(PARTIALS) | {"index.template.html"}


def load_partial(name: str) -> str:
    path = ROOT / name
    if not path.exists():
        sys.exit(f"Missing partial: {path}")
    return path.read_text(encoding="utf-8").rstrip("\n")


def mark_active(header_html: str, page_name: str) -> str:
    """Add class="active" to the nav link pointing at the current page."""
    return header_html.replace(
        f'<a href="{page_name}">',
        f'<a class="active" href="{page_name}">',
        1,
    )


def main() -> None:
    header = load_partial("header.html")
    footer = load_partial("footer.html")

    pages = sorted(p for p in ROOT.glob("*.html") if p.name not in SKIP)
    if not pages:
        sys.exit("No HTML pages found to update.")

    for page in pages:
        text = page.read_text(encoding="utf-8")
        original = text

        page_header = mark_active(header, page.name)
        text, n_header = PARTIALS["header.html"].subn(
            lambda _: page_header, text
        )
        text, n_footer = PARTIALS["footer.html"].subn(
            lambda _: footer, text
        )

        if n_header == 0:
            print(f"  ! {page.name}: no <header> block found")
        if n_footer == 0:
            print(f"  ! {page.name}: no <footer> block found")

        if text != original:
            page.write_text(text, encoding="utf-8")
            print(f"  updated {page.name}")
        else:
            print(f"  unchanged {page.name}")


if __name__ == "__main__":
    print("Updating header/footer from partials...")
    main()
    print("Done.")
