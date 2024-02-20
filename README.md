# tmux-language-server

[![readthedocs](https://shields.io/readthedocs/tmux-language-server)](https://tmux-language-server.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/tmux-language-server/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/tmux-language-server/main)
[![github/workflow](https://github.com/Freed-Wu/tmux-language-server/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/tmux-language-server/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/tmux-language-server/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/tmux-language-server)
[![DeepSource](https://deepsource.io/gh/Freed-Wu/tmux-language-server.svg/?show_trend=true)](https://deepsource.io/gh/Freed-Wu/tmux-language-server)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/tmux-language-server/total)](https://github.com/Freed-Wu/tmux-language-server/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/tmux-language-server/latest/total)](https://github.com/Freed-Wu/tmux-language-server/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)
[![github/v](https://shields.io/github/v/release/Freed-Wu/tmux-language-server)](https://github.com/Freed-Wu/tmux-language-server)

[![pypi/status](https://shields.io/pypi/status/tmux-language-server)](https://pypi.org/project/tmux-language-server/#description)
[![pypi/v](https://shields.io/pypi/v/tmux-language-server)](https://pypi.org/project/tmux-language-server/#history)
[![pypi/downloads](https://shields.io/pypi/dd/tmux-language-server)](https://pypi.org/project/tmux-language-server/#files)
[![pypi/format](https://shields.io/pypi/format/tmux-language-server)](https://pypi.org/project/tmux-language-server/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/tmux-language-server)](https://pypi.org/project/tmux-language-server/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/tmux-language-server)](https://pypi.org/project/tmux-language-server/#files)

A language server for [tmux](https://github.com/tmux/tmux)'s tmux.conf.

- [x] [Diagnostic](https://microsoft.github.io/language-server-protocol/specifications/specification-current#diagnostic)
- [x] [Document Link](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_documentLink)
- [x] [Hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_hover)
- [x] [Completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_completion)

![Diagnostic](https://github.com/Freed-Wu/tmux-language-server/assets/32936898/a92a7d41-4ade-486b-98ef-14382d6d4722)

![option](https://github.com/Freed-Wu/tmux-language-server/assets/32936898/631db877-4cde-4b87-9548-c0a66335a83d)

![command](https://github.com/Freed-Wu/tmux-language-server/assets/32936898/a9793a05-7da6-4fcb-88bf-4ca82ccfbfc1)

![Completion](https://github.com/Freed-Wu/tmux-language-server/assets/32936898/eefc7ec5-c8ef-41ac-8194-e939dac7ae36)

See
[![readthedocs](https://shields.io/readthedocs/tmux-language-server)](https://tmux-language-server.readthedocs.io)
to know more.
