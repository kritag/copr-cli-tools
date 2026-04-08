# kubeseal

This package installs the upstream prebuilt Linux amd64 `kubeseal` release
binary.

Notes:

- Builds only the client binary, not the controller
- Uses the upstream release artifact to avoid Go toolchain drift on older Fedora
  chroots
- Installs the `kubeseal` binary in `/usr/bin`
