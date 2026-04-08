# obsidian

This package repacks the official upstream Debian release of Obsidian and
installs it under `/opt/Obsidian`.

## Update workflow

1. Bump `Version:` in `obsidian.spec`.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This package currently targets `x86_64` only.
- It follows the upstream bundled-Electron packaging model.
- The launcher wrapper is installed as `/usr/bin/obsidian`.
