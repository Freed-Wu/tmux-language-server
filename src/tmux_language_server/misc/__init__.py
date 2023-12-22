r"""Misc
========
"""
from typing import Any

from bs4.element import NavigableString, Tag
from tree_sitter_lsp.misc import get_soup

ALIAS_PREFIX = "(alias: "


def get_schema() -> dict[str, Any]:
    r"""Get schema.

    :rtype: dict[str, Any]
    """
    soup = get_soup("tmux.1", "groff", "mdoc")
    p = soup.find("p", string="CLIENTS AND SESSIONS")
    items = {}
    while p and p.text != "EXIT MESSAGES":
        b = p.find("b")
        if (
            isinstance(b, Tag)
            and b.text == p.text.split()[0]
            and not isinstance(p, NavigableString)
            and p.attrs.get("style") == "margin-top: 1em"
        ):
            text = p.text.replace("\n", " ")
            name = b.text
            p = p.find_next("p")
            if not p:
                continue
            b = p.find("b")
            if p.text.startswith(ALIAS_PREFIX) and isinstance(b, Tag):
                alias = b.text
                text += "\n" + alias
                p = p.find_next("p")
            else:
                alias = name
            if not p:
                continue
            text += "\n" + p.text.replace("\n", " ")
            items[name] = items[alias] = text
        p = p.find_next("p")
    return items
