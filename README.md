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

To trigger COPR rebuilds automatically after version bumps are pushed, add the
COPR GitHub webhook URL to your GitHub repository webhook settings. In COPR,
copy the URL from `Settings -> Webhooks`, then in GitHub configure a repository
webhook for push events using that URL. The scheduled version update workflow
pushes spec changes to `main`, and GitHub will deliver the push webhook to COPR.

Suggested COPR project name:

- `yourname/cli-tools`

## Next steps

1. Add a spec file for one package under `packages/<name>/`.
2. Build locally with `rpmbuild` or submit directly to COPR.
3. Add automation to track new upstream releases.
