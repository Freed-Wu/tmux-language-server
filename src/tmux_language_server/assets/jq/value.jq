if $type == "string" then
  .properties["set-option"].properties[$texts[0]]
else
  empty
end |
if .enum != null then
  .enum[]
else
  empty
end |
if (if $complete then startswith($text) else . == $text end) | not then
  empty
end |
{
  label: .,
  insert_text: .,
  kind: $enums.CompletionItemKind.Constant,
}
