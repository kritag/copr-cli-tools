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

## Version updates

Local bump for one package:

```bash
scripts/bump-version.sh yq 4.52.4
```

Update one package from the latest GitHub release:

```bash
scripts/update-from-github-release.sh yq
```

Packages that support release tracking have a `packages/<name>/upstream.env`
file. The GitHub Actions workflow in
`.github/workflows/update-package-versions.yml` can run on a schedule or by
manual dispatch to bump tracked package versions automatically. This includes
`oc`, which is updated from the OpenShift mirror rather than GitHub releases.

When a spec file changes on `main`, `.github/workflows/trigger-copr-rebuild.yml`
can trigger a COPR rebuild through your project's webhook URL. Configure the
`COPR_WEBHOOK_URL` GitHub Actions secret with the webhook from
`Settings -> Webhooks` in your COPR project.

Suggested COPR project name:

- `yourname/cli-tools`

## Next steps

1. Add a spec file for one package under `packages/<name>/`.
2. Build locally with `rpmbuild` or submit directly to COPR.
3. Add automation to track new upstream releases.
