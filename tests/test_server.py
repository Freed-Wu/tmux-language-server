import os

from tmux_language_server.server import TmuxLanguageServer as Server

server = Server("")
file = os.path.join(os.path.dirname(__file__), "tmux.conf")


class Test:
    @staticmethod
    def test_check() -> None:
        diagnostics = server.lint(file)[file]
        assert len(diagnostics)

    @staticmethod
    def test_complete() -> None:
        contents = server.lookup("option", "set-titles")["set-titles"]
        assert len(contents)
