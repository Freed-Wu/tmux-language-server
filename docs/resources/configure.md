# Configure

See customization in
<https://tmux-language-server.readthedocs.io/en/latest/api/tmux-language-server.html#tmux_language_server.server.get_document>.

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "tmux": {
      "command": "tmux-language-server",
      "filetypes": [
        "tmux"
      ],
      "initializationOptions": {
        "method": "builtin"
      }
    }
  }
}
```

### [vim-lsp](https://github.com/prabirtmuxrestha/vim-lsp)

```vim
if executable('tmux-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'tmux',
          \ 'cmd': {server_info->['tmux-language-server']},
          \ 'whitelist': ['tmux'],
          \ 'initialization_options': {
          \   'method': 'builtin',
          \ },
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "tmux.conf" },
  callback = function()
    vim.lsp.start({
      name = "tmux",
      cmd = { "tmux-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "tmux-language-server")))
  :activation-fn (lsp-activate-on "tmux.conf")
  :server-id "tmux")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "tmux": {
      "command": [
        "tmux-language-server"
      ],
      "enabled": true,
      "selector": "source.tmux"
    }
  }
}
```
