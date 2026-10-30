%global debug_package %{nil}
%global _build_id_links none

Name:           slack
Version:        4.53.276
Release:        3%{?dist}
Summary:        Team communication app for Linux

License:        LicenseRef-Slack
URL:            https://slack.com/release-notes/linux
Source0:        https://downloads.slack-edge.com/desktop-releases/linux/x64/%{version}/slack-desktop-%{version}-amd64.deb
Source1:        slack
Source2:        patch-asar.py
Source3:        slack-font.js
Source4:        font.css
Source5:        fonts/Geist-VF.ttf
Source6:        fonts/Geist-Italic-VF.ttf
Source7:        fonts/GeistMono-Regular.ttf
Source8:        fonts/GeistMono-Bold.ttf
Source9:        fonts/GeistMono-Italic.ttf
Source10:       fonts/GeistMono-BoldItalic.ttf

ExclusiveArch:  x86_64
BuildRequires:  binutils
BuildRequires:  python3
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
# Inject user-editable CSS (/etc/slack/font.css) into every window; fails the build if upstream moves boot.bundle.cjs
python3 -I %{SOURCE2} %{buildroot}%{_prefix}/lib/slack/resources/app.asar dist/boot.bundle.cjs %{SOURCE3}
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/slack/font.css
install -Dpm0644 -t %{buildroot}%{_datadir}/fonts/slack-geist %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10}
install -Dpm0644 usr/share/applications/slack.desktop \
  %{buildroot}%{_datadir}/applications/slack.desktop
install -Dpm0644 usr/share/pixmaps/slack.png \
  %{buildroot}%{_datadir}/pixmaps/slack.png
sed -i 's|^Icon=.*|Icon=slack|' %{buildroot}%{_datadir}/applications/slack.desktop
install -Dpm0644 usr/lib/slack/LICENSE \
  %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/slack
%config(noreplace) %{_sysconfdir}/slack/font.css
%{_prefix}/lib/slack
%{_datadir}/fonts/slack-geist
%{_datadir}/applications/slack.desktop
%{_datadir}/pixmaps/slack.png
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Kristian Tagesen <kristian@example.invalid> - 4.49.81-2
- Normalize desktop icon entry to Icon=slack
- Prune bundled source payload under /usr/lib/slack/src
- Keep wrapper launcher so bundled shared libraries resolve correctly

* Tue Apr 14 2026 Kristian Tagesen <kristian@example.invalid> - 4.49.81-1
- Initial package
