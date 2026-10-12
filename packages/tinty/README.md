# tinty

This package builds `tinty` from the latest upstream `main` commit, not from
tagged releases (the last release is months behind).

## Update workflow

1. Run `scripts/update-from-github-release.sh tinty`. It rewrites `%global commit`
   and `Version` in `tinty.spec` to the current branch head.
2. Commit and push.

The scheduled update workflow does this automatically.

## Notes

- Version format: `<Cargo.toml version>^<commit date>git<short sha>`.
- Shell completions come from `contrib/completion/` in the source tree.
