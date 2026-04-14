%global debug_package %{nil}
%global keybase_build 20260408161357.70cbb6ec7c

Name:           keybase
Version:        6.6.2
Release:        4%{?dist}
Summary:        Meta package for Keybase CLI, KBFS, and GUI

License:        BSD-3-Clause
URL:            https://keybase.io
Source0:        https://prerelease.keybase.io/deb/pool/main/k/keybase/keybase_%{version}-%{keybase_build}_amd64.deb
Source1:        keybase-meta.txt

BuildRequires:  binutils
BuildRequires:  tar
BuildRequires:  xz

Requires:       keybase-cli%{?_isa} = %{version}-%{release}
Requires:       kbfs%{?_isa} = %{version}-%{release}
Requires:       keybase-gui%{?_isa} = %{version}-%{release}

ExclusiveArch:  x86_64

%description
Meta package that installs the full Keybase stack:
CLI, filesystem integration (KBFS), and GUI.

%package -n keybase-cli
Summary:        Keybase CLI tools and user services
Requires:       gnupg2
Requires:       lsof
Requires:       procps-ng
Requires:       psmisc

%description -n keybase-cli
Command-line utilities and core user services for Keybase.

%package -n kbfs
Summary:        Keybase filesystem integration
Requires:       keybase-cli%{?_isa} = %{version}-%{release}
Requires:       fuse

%description -n kbfs
KBFS binaries and user services for Keybase filesystem mounts.

%package -n keybase-gui
Summary:        Keybase desktop GUI
Requires:       alsa-lib
Requires:       gtk3
Requires:       kbfs%{?_isa} = %{version}-%{release}
Requires:       keybase-cli%{?_isa} = %{version}-%{release}
Requires:       libXScrnSaver
Requires:       libXtst
Requires:       nss
Requires:       xdg-utils

%description -n keybase-gui
Desktop GUI package for Keybase, including bundled Electron runtime and app assets.

%prep
rm -rf rootfs
mkdir rootfs
cd rootfs
ar x %{SOURCE0}
tar -xJf data.tar.xz

%build

%install
mkdir -p %{buildroot}
cp -a rootfs/usr %{buildroot}/
cp -a rootfs/etc %{buildroot}/
cp -a rootfs/opt %{buildroot}/

# Drop Debian-specific repository setup.
rm -rf %{buildroot}%{_sysconfdir}/apt

# Meta package payload.
install -Dpm0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/README.meta

%files
%doc %{_docdir}/%{name}/README.meta

%files -n keybase-cli
%{_bindir}/kbnm
%{_bindir}/keybase
%{_bindir}/keybase-redirector
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/io.keybase.kbnm.json
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/io.keybase.kbnm.json
/usr/lib/mozilla/native-messaging-hosts/io.keybase.kbnm.json
/usr/share/keyrings/keybase.asc
/usr/lib/systemd/user/keybase-redirector.service
/usr/lib/systemd/user/keybase.service

%files -n kbfs
%{_bindir}/git-remote-keybase
%{_bindir}/kbfsfuse
/usr/lib/systemd/user/kbfs.service

%files -n keybase-gui
%{_bindir}/run_keybase
/usr/lib/systemd/user/keybase.gui.service
%{_datadir}/applications/keybase.desktop
%doc %{_docdir}/%{name}/changelog.Debian.gz
%{_datadir}/icons/hicolor/*/apps/keybase.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-saltpack.png
%{_datadir}/mime/packages/x-saltpack.xml
/opt/keybase

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 6.6.2-1
- Initial split package (meta + cli + kbfs + gui)
- Source from official upstream Debian artifact

* Tue Apr 14 2026 Codex <codex@example.invalid> - 6.6.2-2
- Replace %{_userunitdir} with explicit systemd user unit paths
- Fix COPR build failure in minimal Fedora buildroot

* Tue Apr 14 2026 Codex <codex@example.invalid> - 6.6.2-3
- Include mozilla native messaging host and upstream keyring file
- Remove duplicate LICENSE file listing warning

* Tue Apr 14 2026 Codex <codex@example.invalid> - 6.6.2-4
- Fix mozilla native messaging host path (`/usr/lib`, not `%{_libdir}`)
