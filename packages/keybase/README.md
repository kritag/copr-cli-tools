# keybase

This package is built from Keybase's official Linux `.deb` artifact and split
into RPM subpackages:

- `keybase` (meta package)
- `keybase-cli`
- `kbfs`
- `keybase-gui`

Installing `keybase` pulls in the full stack (CLI + KBFS + GUI).

## Update workflow

1. Bump `Version` in `keybase.spec` to the new upstream release tag.
2. Update `%global keybase_build` to match the build suffix from the Debian
   package index:
   - https://prerelease.keybase.io/deb/dists/stable/main/binary-amd64/Packages
3. Verify `Source0` resolves.
4. Commit and push.
5. Trigger a COPR rebuild for the SCM package.

## Notes

- This package targets `x86_64` only.
- Upstream ships one bundled binary payload; this spec splits it for better
  dependency control while preserving `dnf install keybase` as the all-in-one
  install path.
