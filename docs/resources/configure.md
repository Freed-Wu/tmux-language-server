# Configure

- For windows, change `~/.config` to `~/AppData/Local`
- For macOS, change `~/.config` to `~/Library`

## (Neo)[Vim](https://www.vim.org)

For vim:

- Change `~/.config/nvim` to `~/.vim`
- Change `init.vim` to `vimrc`

### [coc.nvim](https://github.com/neoclide/coc.nvim)

`~/.config/nvim/coc-settings.json`:

```json
{
  "languageserver": {
    "tmux": {
      "command": "tmux-language-server",
      "filetypes": [
        "tmux"
      ]
    }
  }
}
```

### [vim-lsp](https://github.com/prabirshrestha/vim-lsp)

`~/.config/nvim/init.vim`:

```vim
if executable('tmux-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'tmux',
          \ 'cmd': {server_info->['tmux-language-server']},
          \ 'whitelist': ['tmux'],
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

`~/.config/nvim/init.lua`:

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "tmux.conf", ".tmux.conf" },
  callback = function()
    vim.lsp.start({
      name = "tmux",
      cmd = { "tmux-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

`~/.emacs.d/init.el`:

```lisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "tmux-language-server")))
  :activation-fn (lsp-activate-on "tmux.conf" ".tmux.conf" )
  :server-id "tmux")))
```

## [Helix](https://helix-editor.com/)

`~/.config/helix/languages.toml`:

```toml
[[language]]
name = "tmux"
language-servers = [ "tmux-language-server",]

[language_server.tmux-language-server]
command = "tmux-language-server"
```

## [KaKoune](https://kakoune.org/)

### [kak-lsp](https://github.com/kak-lsp/kak-lsp)

`~/.config/kak-lsp/kak-lsp.toml`:

```toml
[language_server.tmux-language-server]
filetypes = [ "tmux",]
command = "tmux-language-server"
```

## [Sublime](https://www.sublimetext.com)

`~/.config/sublime-text-3/Packages/Preferences.sublime-settings`:

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

## [Visual Studio Code](https://code.visualstudio.com/)

[An official support of generic LSP client is pending](https://github.com/microsoft/vscode/issues/137885).

### [vscode-glspc](https://gitlab.com/ruilvo/vscode-glspc)

`~/.config/Code/User/settings.json`:

```json
{
  "glspc.serverPath": "tmux-language-server",
  "glspc.languageId": "tmux"
}
```
