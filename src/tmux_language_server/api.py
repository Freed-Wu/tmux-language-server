r"""Api
=======
"""
import os
from gzip import decompress
from shlex import split
from subprocess import check_output  # nosec: B404

from bs4 import BeautifulSoup, FeatureNotFound
from bs4.element import NavigableString, Tag
from platformdirs import site_data_dir

ALIAS_PREFIX = "(alias: "


def init_document() -> dict[str, str]:
    r"""Init document.

    :rtype: dict[str, str]
    """
    with open(
        os.path.join(os.path.join(site_data_dir("man"), "man1"), "tmux.1.gz"),
        "rb",
    ) as f:
        text = decompress(f.read()).decode()
    html = check_output(  # nosec: B603
        split("groff -mman -Thtml"), input=text.encode()
    )
    try:
        soup = BeautifulSoup(html, "lxml")
    except FeatureNotFound:
        soup = BeautifulSoup(html, "html.parser")
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
