# slack

This package repacks the official Linux amd64 Slack Debian package.

## Update workflow

1. Bump `Version` in `slack.spec`.
2. Confirm the source archive naming still matches the expected pattern.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.

## Notes

- This spec currently targets `x86_64`.
- The package installs upstream files from the Slack Debian package.
- The upstream auto-update cron job from the Debian package is intentionally
  not installed; updates should come from RPM/COPR.
