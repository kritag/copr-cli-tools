# flavours

This package builds `flavours` from the upstream source archive.

## Update workflow

1. Bump `Version` in `flavours.spec`.
2. Confirm source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- Shell completions are generated during `%build` from the compiled binary.
