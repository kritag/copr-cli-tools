# protonplus

This package builds ProtonPlus from the upstream GitHub tag tarball with
meson.

## Update workflow

1. Run `scripts/update-from-github-release.sh protonplus` to bump the version.
2. Check that the BuildRequires still match upstream `src/meson.build`.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.
