%global debug_package %{nil}
%global _build_id_links none

Name:           slack
Version:        4.49.81
Release:        2%{?dist}
Summary:        Team communication app for Linux

License:        LicenseRef-Slack
URL:            https://slack.com/release-notes/linux
Source0:        https://downloads.slack-edge.com/desktop-releases/linux/x64/%{version}/slack-desktop-%{version}-amd64.deb
Source1:        slack

ExclusiveArch:  x86_64
BuildRequires:  binutils
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  zstd
Requires:       alsa-lib
Requires:       at-spi2-core
Requires:       gtk3
Requires:       libnotify
Requires:       libsecret
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nss
Requires:       xdg-utils

%description
Slack is a team communication and collaboration app.

This package repacks the official upstream Debian package and installs the
bundled Electron application under /usr/lib/slack.

%prep
%setup -q -T -c -n %{name}-%{version}
cp -p %{SOURCE0} .
ar x slack-desktop-%{version}-amd64.deb
if [ -f data.tar.xz ]; then
  tar -xJf data.tar.xz
elif [ -f data.tar.zst ]; then
  unzstd -c data.tar.zst | tar -xf -
else
  tar -xf data.tar.*
fi

%install
install -Dpm0755 %{SOURCE1} %{buildroot}%{_bindir}/slack
mkdir -p %{buildroot}%{_prefix}/lib
cp -a usr/lib/slack %{buildroot}%{_prefix}/lib/
rm -rf %{buildroot}%{_prefix}/lib/slack/src
install -Dpm0644 usr/share/applications/slack.desktop \
  %{buildroot}%{_datadir}/applications/slack.desktop
install -Dpm0644 usr/share/pixmaps/slack.png \
  %{buildroot}%{_datadir}/pixmaps/slack.png
sed -i 's|^Icon=.*|Icon=slack|' %{buildroot}%{_datadir}/applications/slack.desktop
install -Dpm0644 usr/lib/slack/LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/slack
%{_prefix}/lib/slack
%{_datadir}/applications/slack.desktop
%{_datadir}/pixmaps/slack.png
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 4.49.81-2
- Normalize desktop icon entry to Icon=slack
- Prune bundled source payload under /usr/lib/slack/src
- Keep wrapper launcher so bundled shared libraries resolve correctly

* Tue Apr 14 2026 Codex <codex@example.invalid> - 4.49.81-1
- Initial package
