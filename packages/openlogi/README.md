# openlogi

This package repacks the official upstream `amd64`/`arm64` RPM from
[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi). It provides
`openlogi`, `openlogi-agent`, `openlogi-desktop` and `openlogi-overlay`.

## Update workflow

1. Bump `Version` in `openlogi.spec` (the daily workflow does this).
2. Commit and push.
3. Trigger a COPR rebuild for the SCM package.

## Notes

- The udev rule is moved from `/etc/udev/rules.d` to `/usr/lib/udev/rules.d`.
- After install: `systemctl --user enable --now openlogi-agent.service`.
