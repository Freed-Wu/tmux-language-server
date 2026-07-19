if $type == "option" then
  .properties["set-option"].properties
elif $type == "command" or $cursor[1] == 0 then
  .properties
else
  {}
end | to_entries[] |
if .key | (if $complete then startswith($text) else . == $text end) then
  {
    label: .key,
    insert_text: .key,
    kind: (
      if $type == "option" then
        $enums.CompletionItemKind.Variable
      elif $type == "command" then
        $enums.CompletionItemKind.Keyword
      else
        $enums.CompletionItemKind.Constant
      end
    ),
    documentation: {kind: "markdown", value: .value.description}
  }
else
  empty
end
