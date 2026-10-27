# hazelnut

This package installs the upstream Linux `x86_64`/`aarch64` (glibc) release tarball.
It provides `hazelnut` (TUI) and `hazelnutd` (daemon).

## Update workflow

1. Bump `Version` in `hazelnut.spec`.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.
