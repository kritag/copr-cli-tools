%global debug_package %{nil}

Name:           helm
Version:        4.1.4
Release:        2%{?dist}
Summary:        Kubernetes package manager

License:        Apache-2.0
URL:            https://github.com/helm/helm
Source0:        %{url}/releases/download/v%{version}/helm-v%{version}-linux-amd64.tar.gz
Source1:        https://raw.githubusercontent.com/helm/helm/v%{version}/LICENSE

BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

Requires:       glibc
ExclusiveArch:  x86_64

%description
Helm is a package manager for Kubernetes.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 linux-amd64/helm %{buildroot}%{_bindir}/helm
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/helm completion bash > %{buildroot}%{_datadir}/bash-completion/completions/helm
%{buildroot}%{_bindir}/helm completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_helm
%{buildroot}%{_bindir}/helm completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/helm.fish

%files
%{_bindir}/helm
%{_datadir}/bash-completion/completions/helm
%{_datadir}/zsh/site-functions/_helm
%{_datadir}/fish/vendor_completions.d/helm.fish
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 4.1.4-2
- Repackage upstream release binary instead of building from source
- Keep shell completion generation during install

* Thu Mar 26 2026 Codex <codex@example.invalid> - 4.1.3-1
- Initial package
