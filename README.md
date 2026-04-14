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
- lucidglyph
- lesspipe
- obsidian
- oh-my-posh
- sops
- slack
- stern
- flux
- flavours
- kubeconform
- bat-extras
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
manual dispatch to bump tracked package versions automatically, commit the
updated spec files, and immediately submit COPR builds with
`copr-cli build-package --enable-net on`. This includes `oc`, which is updated
from the OpenShift mirror rather than GitHub releases.

`.github/workflows/build-copr-packages.yml` remains available for manual
rebuilds or direct pushes to `main`, but scheduled version bumps no longer rely
on a second workflow being triggered by the updater's bot push. Configure a
`COPR_CONFIG` GitHub Actions secret containing your `copr-cli` config file
contents so either workflow can authenticate to Copr.

To enforce network-enabled builds for all packages in the project (including
manual rebuilds in Copr), set the project default:

```bash
copr-cli modify bonvaffel/cli-tools --enable-net on
```

Suggested COPR project name:

- `yourname/cli-tools`

## Next steps

1. Add a spec file for one package under `packages/<name>/`.
2. Build locally with `rpmbuild` or submit directly to COPR.
3. Add automation to track new upstream releases.
