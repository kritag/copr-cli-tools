# kubecolor

This package builds `kubecolor` from the upstream source archive.

## Update workflow

1. Bump `Version` in `kubecolor.spec`.
2. Confirm source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- `kubectl` is required at runtime.
