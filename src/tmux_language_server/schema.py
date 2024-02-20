r"""Schema
==========
"""

from dataclasses import dataclass

from lsprotocol.types import Position, Range
from tree_sitter import Node
from tree_sitter_lsp import UNI
from tree_sitter_lsp.schema import Trie

DIRECTIVES = {
    "set_option_directive",
    "source_file_directive",
}


@dataclass
class TmuxTrie(Trie):
    r"""Tmux Trie."""

    value: dict[str, "Trie"] | list["Trie"] | str  # type: ignore

    @classmethod
    def from_node(cls, node: Node, parent: "Trie | None") -> "Trie":
        r"""From node.

        :param node:
        :type node: Node
        :param parent:
        :type parent: Trie | None
        :rtype: "Trie"
        """
        if node.type == "value":
            return cls(
                UNI.node2range(node), parent, UNI.node2text(node).strip("'\"")
            )
        if node.type == "file":
            trie = cls(Range(Position(0, 0), Position(1, 0)), parent, {})
            for child in node.children:
                if child.type not in DIRECTIVES:
                    continue
                # directive name
                _type = child.type.split("_directive")[0].replace("_", "-")
                # add directive name to trie.value if it doesn't exist
                _value: dict[str, Trie] = trie.value  # type: ignore
                if _type not in _value:
                    trie.value[_type] = cls(  # type: ignore
                        UNI.node2range(child),
                        trie,
                        {} if _type != "source-file" else [],
                    )
                # the dictionary's key corresponding to directive name
                subtrie: Trie = trie.value[_type]  # type: ignore
                # currently, only support set and source
                # set is a dict, source is a list
                value = subtrie.value  # type: ignore
                # fill subtrie.value
                if child.type == "set_option_directive":
                    value: dict[str, Trie]
                    value[UNI.node2text(child.children[-2])] = cls.from_node(
                        child.children[-1], subtrie
                    )
                elif child.type == "source_file_directive":
                    value += [  # type: ignore
                        cls(
                            UNI.node2range(child.children[1]),
                            subtrie,
                            UNI.node2text(child.children[1]),
                        )
                    ]
            return trie
        raise NotImplementedError(node.type)
