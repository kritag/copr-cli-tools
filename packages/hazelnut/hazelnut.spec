%global debug_package %{nil}
%global __strip /bin/true

Name:           hazelnut
Version:        0.3.0
Release:        1%{?dist}
Summary:        Terminal-based automated file organizer inspired by Hazel

License:        GPL-3.0-only
URL:            https://github.com/ricardodantas/hazelnut
Source0:        %{url}/releases/download/v%{version}/hazelnut-%{version}-%{_arch}-unknown-linux-gnu.tar.gz
Source1:        https://raw.githubusercontent.com/ricardodantas/hazelnut/v%{version}/LICENSE
Source2:        https://raw.githubusercontent.com/ricardodantas/hazelnut/v%{version}/README.md

ExclusiveArch:  x86_64 aarch64

%description
hazelnut watches folders and organizes files with rules. It ships a terminal UI
(hazelnut) and a background daemon (hazelnutd).

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 hazelnut %{buildroot}%{_bindir}/hazelnut
install -Dpm0755 hazelnutd %{buildroot}%{_bindir}/hazelnutd
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.md

%files
%{_bindir}/hazelnut
%{_bindir}/hazelnutd
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md

%changelog
* Tue Oct 27 2026 Kristian Tagesen <kristian@example.invalid> - 0.3.0-1
- Initial package from upstream Linux x86_64/aarch64 release tarball
