# dotbot

This package builds `dotbot` from the upstream GitHub tag tarball using the
Fedora Python packaging macros. It is `noarch`; `PyYAML` is pulled in
automatically as a runtime dependency.

## Update workflow

1. Run `scripts/update-from-github-release.sh dotbot` to bump the version.
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- The test suite is not run: it needs git submodules and git metadata that the
  tag tarball lacks.
