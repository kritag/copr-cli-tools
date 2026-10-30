%global debug_package %{nil}
%global __strip /bin/true

Name:           openlogi
Version:        0.8.19
Release:        1%{?dist}
Summary:        Local-first companion for Logitech HID++ peripherals

License:        Apache-2.0 OR MIT
URL:            https://github.com/AprilNEA/OpenLogi
Source0:        %{url}/releases/download/v%{version}/openlogi-v%{version}-linux-amd64.rpm
Source1:        %{url}/releases/download/v%{version}/openlogi-v%{version}-linux-arm64.rpm

ExclusiveArch:  x86_64 aarch64
BuildRequires:  cpio
BuildRequires:  rpm
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
OpenLogi is an open-source, local-first alternative to Logi Options+ for
remapping buttons and adjusting DPI and SmartShift on Logitech HID++ devices.
No account, no telemetry; configuration lives in a plain TOML file.

This package repacks the official upstream RPM. After installing, enable the
background agent with: systemctl --user enable --now openlogi-agent.service

%prep
%autosetup -c -T
%ifarch x86_64
rpm2cpio %{SOURCE0} | cpio -idm --quiet
%else
rpm2cpio %{SOURCE1} | cpio -idm --quiet
%endif

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}/
# Upstream installs the udev rules under /etc; vendor rules belong in /usr/lib.
install -Dpm0644 etc/udev/rules.d/70-openlogi.rules \
  %{buildroot}%{_udevrulesdir}/70-openlogi.rules

%post
%udev_rules_update
udevadm trigger --subsystem-match=hidraw --subsystem-match=input >/dev/null 2>&1 || :

%postun
%udev_rules_update

%files
%{_bindir}/openlogi
%{_bindir}/openlogi-agent
%{_bindir}/openlogi-desktop
%{_bindir}/openlogi-overlay
%{_userunitdir}/openlogi-agent.service
%{_udevrulesdir}/70-openlogi.rules
%{_datadir}/applications/openlogi.desktop
%{_datadir}/icons/hicolor/*/apps/openlogi.png
%license %{_licensedir}/%{name}/LICENSE-APACHE
%license %{_licensedir}/%{name}/LICENSE-MIT

%changelog
* Thu Oct 29 2026 Kristian Tagesen <kristian@example.invalid> - 0.8.18-1
- Initial package from upstream Linux amd64/arm64 RPM
