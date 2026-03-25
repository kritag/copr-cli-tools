# copr-cli-tools

RPM packaging repo for a personal Fedora COPR that carries selected CLI tools.

Current target packages:

- argocd
- kubectl
- krew
- kubectx
- kubeseal
- helm
- lazygit
- lesspipe
- oh-my-posh
- sops
- stern
- vivid
- yq
- zoxide
- eza

## Layout

- `packages/<name>/` contains packaging files for one tool
- `scripts/` contains local helper scripts for version bumps and builds

Suggested COPR project name:

- `yourname/cli-tools`

## Next steps

1. Add a spec file for one package under `packages/<name>/`.
2. Build locally with `rpmbuild` or submit directly to COPR.
3. Add automation to track new upstream releases.
