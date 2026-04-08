# lesspipe

This package builds `lesspipe` from the upstream source release and installs
the Arch-style `/etc/profile.d/lesspipe.sh` snippet.

## Update workflow

1. Run `scripts/update-from-github-release.sh lesspipe` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- This package is `noarch`.
- The executable is built from the upstream source tarball.
- `/etc/profile.d/lesspipe.sh` sets `LESSOPEN='|/usr/bin/lesspipe.sh %s'`.
