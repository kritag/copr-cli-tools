# zoxide

This package builds `zoxide` from the upstream source release.

## Update workflow

1. Bump `Version` in `zoxide.spec`.
2. Confirm the source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- COPR builds need networking enabled because Cargo fetches crates during the
  build.
