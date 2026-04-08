# oh-my-posh

This package installs the upstream Linux `x86_64` release binary and ships the
built-in theme files from the source archive.

## Update workflow

1. Run `scripts/update-from-github-release.sh oh-my-posh` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec targets `x86_64`.
- The package installs the upstream `oh-my-posh` binary, bundled themes, and the license.
- Using the release binary avoids Fedora 43 build failures caused by the newer Go toolchain requirement.
