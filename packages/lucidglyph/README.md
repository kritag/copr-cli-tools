# lucidglyph

This package installs `lucidglyph` font rendering configuration files.

## Update workflow

1. Bump `Version` in `lucidglyph.spec`.
2. Confirm source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This package is `noarch`.
- It ships fontconfig and environment configuration files only.
