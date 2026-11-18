# spotifast

Repackages the upstream Linux `x86_64`/`aarch64` (glibc) release tarball.
Nothing is compiled.

## Build

1. `rpmbuild -bb --undefine=_disable_source_fetch spotifast.spec`

## Gotchas

- `%prep` verifies upstream's Ed25519 signature on `checksums.txt`, then the
  tarball's sha256. A bad release fails the build.
- `spotifast-update-public-key.pem` is upstream's `assets/update-public-key.hex`
  as PEM. Regenerate only if upstream rotates the key:
  `printf 302a300506032b6570032100<hex> | xxd -r -p | openssl pkey -pubin -inform DER -outform PEM`
- Runtime libs are dlopen()ed, so they are listed as explicit `Requires`.
- Upstream's `contrib/omarchy` files are not installed.
