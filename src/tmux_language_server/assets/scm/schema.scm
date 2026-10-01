(source_file_directive
  (path
    (string) @source-file.-))

; array options (`type: array` in tmux.json): `set`, `set -a` etc. supply one
; element, so append it. Keep the name list in sync with the schema.
(set_option_directive
  (option) @--option
  (value
    (string) @set-option.-option.-)
  (#match? @--option "^(command-alias|terminal-features|terminal-overrides|user-keys|status-format|update-environment|pane-colours)$"))

(set_option_directive
  (option) @--option
  (value
    (string) @set-option.-option)
  (#not-match? @--option "^(command-alias|terminal-features|terminal-overrides|user-keys|status-format|update-environment|pane-colours)$"))
