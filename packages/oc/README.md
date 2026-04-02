# oc

This package installs the upstream prebuilt `oc` (OpenShift CLI) binary from
the OpenShift mirror.

## Update workflow

1. Run `scripts/update-from-github-release.sh oc` to pull the latest version from
   the OpenShift mirror.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

> **Note:** `openshift/oc` has no proper GitHub releases. This repository updates
> it from the OpenShift mirror instead.

## Notes

- This spec targets `x86_64`.
- The package installs the `oc` binary and generates bash and zsh completion scripts at install time.
