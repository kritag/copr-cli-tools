%global debug_package %{nil}

Name:           flux
Version:        2.8.6
Release:        4%{?dist}
Summary:        Open and extensible continuous delivery solution for Kubernetes

License:        Apache-2.0
URL:            https://github.com/fluxcd/flux2
Source0:        %{url}/releases/download/v%{version}/flux_%{version}_linux_amd64.tar.gz
Source1:        https://raw.githubusercontent.com/fluxcd/flux2/v%{version}/LICENSE

BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

ExclusiveArch:  x86_64

%description
Flux is a GitOps toolkit and command-line interface for managing continuous
delivery on Kubernetes. This package installs the upstream prebuilt CLI
binary.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 flux %{buildroot}%{_bindir}/flux
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/flux completion bash > %{buildroot}%{_datadir}/bash-completion/completions/flux
%{buildroot}%{_bindir}/flux completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_flux
%{buildroot}%{_bindir}/flux completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/flux.fish

%files
%{_bindir}/flux
%{_datadir}/bash-completion/completions/flux
%{_datadir}/zsh/site-functions/_flux
%{_datadir}/fish/vendor_completions.d/flux.fish
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.8.5-4
- Repackage upstream release binary instead of building from source
- Keep shell completion generation during install

* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.8.5-3
- Generate embedded manifests with upstream bundle script
- Add kustomize build dependency

* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.8.5-2
- Stage embedded manifest YAMLs into cmd/flux/manifests before build

* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.8.5-1
- Initial package
