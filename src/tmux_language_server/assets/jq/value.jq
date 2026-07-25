if $nodes[0].type == "string" then
  .properties["set-option"].properties[$nodes[1].text]
else
  empty
end |
if .enum != null then
  .enum[]
else
  empty
end |
if ($nodes[0].text as $text | if $complete then startswith($text) else . == $text end) | not then
  empty
end |
{
  label: .,
  insert_text: .,
  kind: $enums.CompletionItemKind.Constant,
}
