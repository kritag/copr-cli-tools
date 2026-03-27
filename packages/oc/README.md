# oc

This package installs the upstream prebuilt `oc` (OpenShift CLI) binary from
the OpenShift mirror.

## Update workflow

1. Check the latest version at https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/release.txt
2. Run `scripts/bump-version.sh oc <version>` to update the spec.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

> **Note:** `update-from-github-release.sh` does not work for this package —
> `openshift/oc` has no proper GitHub releases. Versions must be bumped manually.

## Notes

- This spec targets `x86_64`.
- The package installs the `oc` binary and generates bash and zsh completion scripts at install time.
