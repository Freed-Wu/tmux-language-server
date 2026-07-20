r"""Server
==========
"""

import os

from lsp_tree_sitter.completer import (
    PathCompleter,
    SchemaCompleter,
    ValueCompleter,
)
from lsp_tree_sitter.linter import PathLinter, SchemaLinter
from lsp_tree_sitter.server import TreeSitterLanguageServer
from tree_sitter import Language, Parser
from tree_sitter_tmux import language as get_language_ptr
from tree_sitter_tmux import queries


class TmuxLanguageServer(TreeSitterLanguageServer):
    def __init__(self, *args, **kwargs) -> None:
        parser = Parser()
        language = Language(get_language_ptr())
        parser.language = language

        assets_path = os.path.join(os.path.dirname(__file__), "assets")
        code_file = os.path.join(assets_path, "jq", "main.jq")
        schema_file = os.path.join(assets_path, "json", "tmux.json")
        schema_completer = SchemaCompleter.from_files(code_file, schema_file)
        code_file = os.path.join(assets_path, "jq", "value.jq")
        value_completer = ValueCompleter.from_files(
            code_file, schema_file, ("^-",)
        )
        path_completer = PathCompleter(
            "path", {"tmux.conf": "tmux", "**/tmux.conf": "tmux"}
        )
        path_linter = PathLinter.from_queries(language, queries)
        schema_linter = SchemaLinter.from_queries(
            language, queries, schema_file
        )

        super().__init__(
            parser,
            (schema_linter, path_linter),
            (schema_completer, value_completer, path_completer),
            *args,
            **kwargs,
        )
