# vivid

This package installs the upstream Linux `x86_64` release binary.

## Update workflow

1. Bump `Version` in `vivid.spec`.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- Themes and file-type config are embedded in the binary via `rust-embed`; no data directory is installed.
- This spec currently targets `x86_64`.
- Using the release binary avoids Rust toolchain drift during COPR builds.
