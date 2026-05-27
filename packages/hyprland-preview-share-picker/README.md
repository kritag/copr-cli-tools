# hyprland-preview-share-picker

This package builds `hyprland-preview-share-picker` from the upstream source archive.

## Update workflow

1. Bump `Version` in `hyprland-preview-share-picker.spec`.
2. Check if the `lib/hyprland-protocols` submodule SHA has changed for the new release:
   ```
   curl -s "https://api.github.com/repos/WhySoBad/hyprland-preview-share-picker/git/trees/v<NEW_VERSION>?recursive=1" \
     | jq '.tree[] | select(.path == "lib/hyprland-protocols")'
   ```
3. If the submodule SHA changed, update `Source1:` to point to the matching
   `hyprland-protocols` tagged release and update the comment.
4. Commit and push.
5. Trigger a COPR rebuild for the SCM package.

## Notes

- The package bundles the `lib/hyprland-protocols` git submodule as `Source1`
  so the build is fully reproducible without git access.
- `cargo fetch --locked` is run in `%prep` on the COPR build server; COPR
  builds must have networking enabled (`--enable-net on`).
- Rust 2024 edition (stabilised in Rust 1.85) is required — no nightly
  toolchain needed.
- `slurp` is an optional runtime tool used as the default region selector;
  it is listed as `Suggests`.
