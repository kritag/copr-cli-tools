# flux

This package builds `flux` from the upstream source release.

## Update workflow

1. Run `scripts/update-from-github-release.sh flux` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec targets `x86_64`.
- COPR builds need networking enabled because Go dependencies are resolved
  during the build.
