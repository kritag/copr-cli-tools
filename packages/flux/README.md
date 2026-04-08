# flux

This package installs the upstream prebuilt Linux amd64 `flux` release binary.

## Update workflow

1. Run `scripts/update-from-github-release.sh flux` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec targets `x86_64`.
- Shell completions are generated from the packaged binary during `%install`.
- Using the upstream release binary avoids Fedora toolchain drift, including the
  Go version mismatch seen on Fedora 43.
