# bat-extras

This package installs the upstream `bat-extras` release archive.

## Update workflow

1. Run `scripts/update-from-github-release.sh bat-extras` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This package is `noarch`.
- It installs the published release zip rather than rebuilding from the git
  repository and submodules.
