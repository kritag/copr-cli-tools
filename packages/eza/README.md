# eza

This package builds `eza` from the upstream source archive.

## Update workflow

1. Bump `Version` in `eza.spec`.
2. Confirm the source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- COPR builds need networking enabled because Cargo dependencies are fetched
  during the build.
