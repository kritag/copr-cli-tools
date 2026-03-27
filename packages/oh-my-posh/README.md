# oh-my-posh

This package builds `oh-my-posh` from the upstream source release.

## Update workflow

1. Run `scripts/update-from-github-release.sh oh-my-posh` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec targets `x86_64`.
- The package installs the `oh-my-posh` binary, bundled themes, and the license.
