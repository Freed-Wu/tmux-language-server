r"""This module can be called by
`python -m <https://docs.python.org/3/library/__main__.html>`_.
"""

import logging
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from contextlib import suppress
from datetime import datetime

from . import __name__ as NAME
from . import __version__

logger = logging.getLogger(__name__)
NAME = NAME.replace("_", "-")
VERSION = rf"""{NAME} {__version__}
Copyright (C) {datetime.now().year}
Written by Wu Zhenyu
"""
EPILOG = """
Report bugs to <wuzhenyu@ustc.edu>.
"""


def get_parser():
    r"""Get a parser for unit test."""
    parser = ArgumentParser(
        epilog=EPILOG,
        formatter_class=RawDescriptionHelpFormatter,
    )
    with suppress(ImportError):
        import shtab

        shtab.add_argument_to(parser)
    parser.add_argument("--version", version=VERSION, action="version")
    parser.add_argument(
        "--generate-schema",
        choices=["tmux"],  # type: ignore
        help="generate schema in an output format",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="generated json's indent",
    )
    parser.add_argument(
        "--check",
        nargs="*",
        default={},
        help="check file's errors and warnings",
    )
    parser.add_argument(
        "--color",
        choices=["auto", "always", "never"],
        default="auto",
        help="when to display color, default: %(default)s",
    )
    parser.add_argument(
        "--convert",
        nargs="*",
        default={},
        help="convert files to output format",
    )
    parser.add_argument(
        "--output-format",
        choices=["json", "yaml", "toml"],
        default="json",
        help="output format: %(default)s",
    )
    return parser


def main():
    r"""Parse arguments and provide shell completions."""
    args = get_parser().parse_args()

    if args.generate_schema or args.check or args.convert:
        from tree_sitter_lsp.diagnose import check
        from tree_sitter_lsp.utils import pprint
        from tree_sitter_tmux import parser

        from .finders import DIAGNOSTICS_FINDER_CLASSES
        from .schema import TmuxTrie

        if args.generate_schema:
            from .misc import get_schema

            pprint(
                get_schema(),
                filetype=args.output_format,
                indent=args.indent,
            )
            return None
        for file in args.convert:
            pprint(
                TmuxTrie.from_file(file, parser.parse).to_json(),
                filetype=args.output_format,
                indent=args.indent,
            )
        exit(
            check(
                args.check,
                parser.parse,
                DIAGNOSTICS_FINDER_CLASSES,
                None,
                args.color,
            )
        )

    from .server import TmuxLanguageServer

    TmuxLanguageServer(NAME, __version__).start_io()


if __name__ == "__main__":
    main()
