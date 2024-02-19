r"""Finders
===========
"""

from dataclasses import dataclass

from lsprotocol.types import DiagnosticSeverity
from tree_sitter_lsp.finders import ErrorFinder, QueryFinder

from .utils import get_query


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


DIAGNOSTICS_FINDER_CLASSES = [
    ErrorFinder,
]
