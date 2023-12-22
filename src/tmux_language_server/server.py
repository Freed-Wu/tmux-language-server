r"""Server
==========
"""
import re
from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    Hover,
    MarkupContent,
    MarkupKind,
    Position,
    Range,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer

from .utils import get_schema


class TmuxLanguageServer(LanguageServer):
    r"""Tmux language server."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        r"""Init.

        :param args:
        :type args: Any
        :param kwargs:
        :type kwargs: Any
        :rtype: None
        """
        super().__init__(*args, **kwargs)

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            word, _range = self._cursor_word(
                params.text_document.uri, params.position, True
            )
            properties = get_schema().get("properties", {})
            description = properties.get(word, {}).get("description", "")
            if not description:
                return None
            return Hover(
                MarkupContent(MarkupKind.Markdown, description), _range
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            word, _ = self._cursor_word(
                params.text_document.uri, params.position, False
            )
            properties = get_schema().get("properties", {})
            items = [
                CompletionItem(
                    x,
                    kind=CompletionItemKind.Function,
                    documentation=MarkupContent(
                        MarkupKind.Markdown, property.get("description", "")
                    ),
                    insert_text=x,
                )
                for x, property in properties.items()
                if x.startswith(word)
            ]
            return CompletionList(False, items)

    def _cursor_line(self, uri: str, position: Position) -> str:
        r"""Cursor line.

        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :rtype: str
        """
        document = self.workspace.get_document(uri)
        return document.source.splitlines()[position.line]

    def _cursor_word(
        self,
        uri: str,
        position: Position,
        include_all: bool = True,
        regex: str = r"\w+",
    ) -> tuple[str, Range]:
        """Cursor word.

        :param self:
        :param uri:
        :type uri: str
        :param position:
        :type position: Position
        :param include_all:
        :type include_all: bool
        :param regex:
        :type regex: str
        :rtype: tuple[str, Range]
        """
        line = self._cursor_line(uri, position)
        for m in re.finditer(regex, line):
            if m.start() <= position.character <= m.end():
                end = m.end() if include_all else position.character
                return (
                    line[m.start() : end],
                    Range(
                        Position(position.line, m.start()),
                        Position(position.line, end),
                    ),
                )
        return (
            "",
            Range(Position(position.line, 0), Position(position.line, 0)),
        )
