# yq

This package installs the upstream prebuilt `yq` binary from GitHub releases.

## Update workflow

1. Bump `Version` in `yq.spec`.
2. Verify the release asset name still matches the expected pattern.
3. Refresh `Source0` if upstream changes naming or archive layout.
4. Build in COPR or locally with `rpmbuild`.

## Notes

- This first spec targets `x86_64` only.
- If you want multi-arch support later, add per-arch source selection for `amd64`/`arm64`.
