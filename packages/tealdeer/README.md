# tealdeer

This package builds `tealdeer` (installed as `tldr`) from the upstream GitHub
tag tarball with cargo. Fedora dropped it after Fedora 44.

## Update workflow

1. Run `scripts/update-from-github-release.sh tealdeer` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.
