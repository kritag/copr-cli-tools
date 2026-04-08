%global debug_package %{nil}

Name:           kubeseal
Version:        0.36.1
Release:        2%{?dist}
Summary:        One-way encrypted Secrets for Kubernetes

License:        Apache-2.0
URL:            https://github.com/bitnami-labs/sealed-secrets
Source0:        %{url}/releases/download/v%{version}/kubeseal-%{version}-linux-amd64.tar.gz
Source1:        https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/v%{version}/LICENSE

Requires:       glibc

ExclusiveArch:  x86_64

%description
kubeseal is a client for creating one-way encrypted Kubernetes Secrets for use
with the sealed-secrets controller. This package installs the upstream
prebuilt CLI binary.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 kubeseal %{buildroot}%{_bindir}/kubeseal
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/kubeseal
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 0.36.1-2
- Repackage upstream release binary instead of building from source

* Thu Mar 26 2026 Codex <codex@example.invalid> - 0.36.1-1
- Initial package
