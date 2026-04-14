# helm

This package installs the upstream Linux `x86_64` release binary.

## Update workflow

1. Bump `Version` in `helm.spec`.
2. Confirm the source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- Shell completions are generated during install from the packaged binary.
- Using the release binary avoids chroot toolchain drift during COPR builds.
