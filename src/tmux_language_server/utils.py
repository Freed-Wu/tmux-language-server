r"""Utils
=========
"""

import json
import os
from typing import Any

from tree_sitter import Language, Parser, Query
from tree_sitter_tmux import language as get_language_ptr

from . import FILETYPE

SCHEMAS = {}
QUERIES = {}
language = Language(get_language_ptr())
parser = Parser()

parser.language = language


def get_query(name: str, filetype: FILETYPE = "tmux") -> Query:
    r"""Get query.

    :param name:
    :type name: str
    :param filetype:
    :type filetype: FILETYPE
    :rtype: Query
    """
    if name not in QUERIES:
        with open(
            os.path.join(
                os.path.dirname(__file__),
                "assets",
                "queries",
                f"{name}{os.path.extsep}scm",
            )
        ) as f:
            text = f.read()
        QUERIES[name] = language.query(text)
    return QUERIES[name]


def get_schema(filetype: FILETYPE = "tmux") -> dict[str, Any]:
    r"""Get schema.

    :param filetype:
    :type filetype: FILETYPE
    :rtype: dict[str, Any]
    """
    if filetype not in SCHEMAS:
        file = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "json",
            f"{filetype}.json",
        )
        with open(file) as f:
            SCHEMAS[filetype] = json.load(f)
    return SCHEMAS[filetype]
