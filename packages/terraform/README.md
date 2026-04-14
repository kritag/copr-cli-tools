# terraform

This package builds `terraform` from the upstream source release.

## Update workflow

1. Bump `Version` in `terraform.spec`.
2. Confirm source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- Bash and zsh completion snippets are maintained in this packaging repo.
