%global debug_package %{nil}

Name:           argocd
Version:        3.3.8
Release:        1%{?dist}
Summary:        Declarative GitOps continuous delivery tool for Kubernetes

License:        Apache-2.0
URL:            https://github.com/argoproj/argo-cd
Source0:        %{url}/releases/download/v%{version}/argocd-linux-amd64
Source1:        https://raw.githubusercontent.com/argoproj/argo-cd/v%{version}/LICENSE

ExclusiveArch:  x86_64

%description
Argo CD is a declarative continuous delivery tool for Kubernetes. This package
installs the upstream prebuilt CLI binary.

%prep
%autosetup -c -T

%build

%install
install -Dpm0755 %{SOURCE0} %{buildroot}%{_bindir}/argocd
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/argocd
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Mar 26 2025 Codex <codex@example.invalid> - 3.3.6-1
- Update to 3.3.6
