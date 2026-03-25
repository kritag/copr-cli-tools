%global debug_package %{nil}

Name:           yq
Version:        4.48.2
Release:        1%{?dist}
Summary:        Portable YAML, JSON, XML, CSV, and TOML processor

License:        MIT
URL:            https://github.com/mikefarah/yq
Source0:        %{url}/releases/download/v%{version}/yq_linux_amd64.tar.gz
Source1:        https://raw.githubusercontent.com/mikefarah/yq/v%{version}/LICENSE

BuildArch:      x86_64
Provides:       yq

%description
yq is a lightweight command-line processor for YAML, JSON, XML, CSV, and TOML
documents. This package installs the upstream prebuilt Linux binary.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%build

%install
install -Dpm0755 yq_linux_amd64 %{buildroot}%{_bindir}/yq
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

if [ -f yq.1 ]; then
    install -Dpm0644 yq.1 %{buildroot}%{_mandir}/man1/yq.1
fi

%files
%{_bindir}/yq
%license %{_licensedir}/%{name}/LICENSE
%{_mandir}/man1/yq.1*

%changelog
* Wed Mar 25 2026 Codex <codex@example.invalid> - 4.48.2-1
- Initial package
