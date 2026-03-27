# vivid

This package builds `vivid` from the upstream source archive.

## Update workflow

1. Bump `Version` in `vivid.spec`.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- Themes and file-type config are embedded in the binary via `rust-embed`; no data directory is installed.
- This spec currently targets `x86_64`.
- COPR builds need networking enabled because Cargo dependencies are fetched during the build.
