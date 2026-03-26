# argocd

This package installs the upstream prebuilt `argocd` Linux release binary from
GitHub.

## Update workflow

1. Bump `Version` in `argocd.spec`.
2. Confirm the release asset naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- The package installs the CLI binary and license.
