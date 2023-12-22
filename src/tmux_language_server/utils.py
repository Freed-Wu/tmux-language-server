r"""Utils
=========
"""
import json
import os
from typing import Any

SCHEMAS = {}


def get_schema(filetype: str = "tmux") -> dict[str, Any]:
    r"""Get schema.

    :param filetype:
    :type filetype: str
    :rtype: dict[str, Any]
    """
    if filetype not in SCHEMAS:
        file = os.path.join(
            os.path.join(
                os.path.join(os.path.dirname(__file__), "assets"),
                "json",
            ),
            f"{filetype}.json",
        )
        with open(file, "r") as f:
            SCHEMAS[filetype] = json.load(f)
    return SCHEMAS[filetype]
