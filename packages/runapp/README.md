# runapp

This package builds `runapp` from the upstream GitHub tag tarball with
`make release`. `-march=native` is disabled so the binary runs on any CPU.

## Update workflow

1. Run `scripts/update-from-github-release.sh runapp` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.
