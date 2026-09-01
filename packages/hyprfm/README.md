# hyprfm

This package builds `hyprfm` from the upstream source release using cmake/ninja.

## Submodules — read before bumping

Upstream vendors two QML dependencies as git submodules:

- `src/qml/Quill` -> `soyeb-jim285/quill`
- `src/qml/icons` -> `soyeb-jim285/quill-icons`

The GitHub release tarball ships these as **empty directories**, and neither
submodule repo is tagged, so both are pinned by commit SHA in
`%global quill_commit` / `%global icons_commit` at the top of the spec.

`scripts/update-from-github-release.sh` only rewrites `Version:`. It will
**not** refresh those SHAs, so after an automated bump the build may still use
the previous release's QML sources. To get the correct pins for a tag:

```sh
git ls-tree v<version> src/qml/ | grep commit
```

Then update both `%global` lines to match.

## Update workflow

1. Bump `Version` in `hyprfm.spec`.
2. Refresh `quill_commit` and `icons_commit` as described above.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- Targets x86_64 and aarch64.
- COPR builds need networking enabled so the submodule tarballs can be fetched.
