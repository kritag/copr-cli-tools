# bibata-cursor-theme

This package installs only the `Bibata-Modern-Classic` cursor theme under:

- `/usr/share/icons/Bibata-Modern-Classic`

It is intentionally scoped to match GNOME setting:

- `org.gnome.desktop.interface cursor-theme='Bibata-Modern-Classic'`

## Update workflow

1. Bump `Version` in `bibata-cursor-theme.spec`.
2. Confirm the release asset still exists:
   `Bibata-Modern-Classic.tar.xz`.
3. Commit and push.
4. Trigger a COPR rebuild for the SCM package.
