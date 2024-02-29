r"""Finders
===========
"""

from dataclasses import dataclass

from lsp_tree_sitter.finders import ErrorFinder, QueryFinder, SchemaFinder
from lsprotocol.types import DiagnosticSeverity

from .schema import TmuxTrie
from .utils import get_query, get_schema


@dataclass(init=False)
class ImportTmuxFinder(QueryFinder):
    r"""Import Tmux finder."""

    def __init__(
        self,
        message: str = "{{uni.get_text()}}: found",
        severity: DiagnosticSeverity = DiagnosticSeverity.Information,
    ):
        r"""Init.

        :param message:
        :type message: str
        :param severity:
        :type severity: DiagnosticSeverity
        """
        query = get_query("import")
        super().__init__(query, message, severity)


@dataclass(init=False)
class TmuxFinder(SchemaFinder):
    r"""Tmuxfinder."""

    def __init__(self) -> None:
        r"""Init.

        :rtype: None
        """
        self.validator = self.schema2validator(get_schema())
        self.cls = TmuxTrie


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorFinder,
    TmuxFinder,
]
