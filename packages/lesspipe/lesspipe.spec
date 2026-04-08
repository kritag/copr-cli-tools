Name:           lesspipe
Version:        2.24
Release:        2%{?dist}
Summary:        Profile hook that enables Fedora's lesspipe integration

License:        GPL-2.0-or-later
URL:            https://www-zeuthen.desy.de/~friebel/unix/lesspipe.html
Source1:        lesspipe.sh

BuildArch:      noarch
Requires:       bash
Requires:       less
Requires:       less-color

%description
Fedora already ships the lesspipe helper binaries and man page in the less and
less-color packages. This package installs the profile snippet that enables the
integration automatically for interactive shell sessions.

%install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/lesspipe.sh

%files
%{_sysconfdir}/profile.d/lesspipe.sh

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.24-2
- Rework package to install only the profile hook on Fedora

* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.24-1
- Initial package
