r"""Server
==========
"""

from typing import Any

from lsprotocol.types import (
    TEXT_DOCUMENT_COMPLETION,
    TEXT_DOCUMENT_DID_CHANGE,
    TEXT_DOCUMENT_DID_OPEN,
    TEXT_DOCUMENT_DOCUMENT_LINK,
    TEXT_DOCUMENT_HOVER,
    CompletionItem,
    CompletionItemKind,
    CompletionList,
    CompletionParams,
    DidChangeTextDocumentParams,
    DocumentLink,
    DocumentLinkParams,
    Hover,
    MarkupContent,
    MarkupKind,
    TextDocumentPositionParams,
)
from pygls.server import LanguageServer
from tree_sitter_lsp.diagnose import get_diagnostics
from tree_sitter_lsp.finders import PositionFinder
from tree_sitter_tmux import parser

from .finders import DIAGNOSTICS_FINDER_CLASSES, ImportTmuxFinder
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
        self.trees = {}

        @self.feature(TEXT_DOCUMENT_DID_OPEN)
        @self.feature(TEXT_DOCUMENT_DID_CHANGE)
        def did_change(params: DidChangeTextDocumentParams) -> None:
            r"""Did change.

            :param params:
            :type params: DidChangeTextDocumentParams
            :rtype: None
            """
            document = self.workspace.get_document(params.text_document.uri)
            self.trees[document.uri] = parser.parse(document.source.encode())
            diagnostics = get_diagnostics(
                document.uri,
                self.trees[document.uri],
                DIAGNOSTICS_FINDER_CLASSES,
                "tmux",
            )
            self.publish_diagnostics(params.text_document.uri, diagnostics)

        @self.feature(TEXT_DOCUMENT_DOCUMENT_LINK)
        def document_link(params: DocumentLinkParams) -> list[DocumentLink]:
            r"""Get document links.

            :param params:
            :type params: DocumentLinkParams
            :rtype: list[DocumentLink]
            """
            document = self.workspace.get_document(params.text_document.uri)
            return ImportTmuxFinder().get_document_links(
                document.uri, self.trees[document.uri]
            )

        @self.feature(TEXT_DOCUMENT_HOVER)
        def hover(params: TextDocumentPositionParams) -> Hover | None:
            r"""Hover.

            :param params:
            :type params: TextDocumentPositionParams
            :rtype: Hover | None
            """
            document = self.workspace.get_document(params.text_document.uri)
            uni = PositionFinder(params.position).find(
                document.uri, self.trees[document.uri]
            )
            if uni is None:
                return None
            text = uni.get_text()
            result = None
            if uni.node.range.start_point[1] == 0:
                result = get_schema()["properties"].get(text)
            elif uni.node.type == "option":
                result = get_schema()["properties"]["set"]["properties"].get(
                    text
                )
            if result is None:
                return None
            return Hover(
                MarkupContent(MarkupKind.Markdown, result["description"]),
                uni.get_range(),
            )

        @self.feature(TEXT_DOCUMENT_COMPLETION)
        def completions(params: CompletionParams) -> CompletionList:
            r"""Completions.

            :param params:
            :type params: CompletionParams
            :rtype: CompletionList
            """
            document = self.workspace.get_document(params.text_document.uri)
            uni = PositionFinder(params.position, right_equal=True).find(
                document.uri, self.trees[document.uri]
            )
            if uni is None:
                return CompletionList(False, [])
            text = uni.get_text()
            if uni.node.range.start_point[1] == 0:
                return CompletionList(
                    False,
                    [
                        CompletionItem(
                            x,
                            kind=CompletionItemKind.Keyword,
                            documentation=MarkupContent(
                                MarkupKind.Markdown, property["description"]
                            ),
                            insert_text=x,
                        )
                        for x, property in get_schema()["properties"].items()
                        if x.startswith(text)
                    ],
                )
            elif uni.node.type == "option":
                return CompletionList(
                    False,
                    [
                        CompletionItem(
                            x,
                            kind=CompletionItemKind.Variable,
                            documentation=MarkupContent(
                                MarkupKind.Markdown, property["description"]
                            ),
                            insert_text=x,
                        )
                        for x, property in get_schema()["properties"]["set"][
                            "properties"
                        ].items()
                        if x.startswith(text)
                    ],
                )
            return CompletionList(False, [])
