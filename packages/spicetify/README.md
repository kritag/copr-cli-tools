# spicetify

This package installs the upstream Linux `x86_64` release tarball.

## Update workflow

1. Bump `Version` in `spicetify.spec`.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- Spicetify finds its `Themes`, `Extensions`, `CustomApps` and `jsHelper`
  directories next to the real executable, so everything lives in
  `/usr/share/spicetify` and `/usr/bin/spicetify` is a symlink.
- Spicetify patches Spotify files. It needs write access to the Spotify install
  directory (for example `sudo chmod a+wr /opt/spotify -R`) and a one-time
  `spicetify backup apply`.
