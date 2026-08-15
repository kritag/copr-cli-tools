# zsh-patina

This package builds `zsh-patina` from the upstream source release using cargo.

## Update workflow

1. Bump `Version` in `zsh-patina.spec`.
2. Confirm the source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec targets x86_64, aarch64, and armv7hl architectures.
- COPR builds need networking enabled because Cargo fetches crates during the build.
- Shell completions are generated during the build from the binary itself.
