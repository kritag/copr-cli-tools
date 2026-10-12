# papirus-folders

This package builds `papirus-folders` from the upstream release archive.

## Update workflow

1. Run `scripts/update-from-github-release.sh papirus-folders`.
2. Commit and push.

## Notes

- Noarch: the tool is a single bash script.
- Requires `papirus-icon-theme` (Fedora package) for the icons it recolors.
- Zsh completion is installed to `site-functions` instead of upstream's `vendor-completions`.
