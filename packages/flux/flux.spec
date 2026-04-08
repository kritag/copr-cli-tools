Name:           flux
Version:        2.8.5
Release:        1%{?dist}
Summary:        Open and extensible continuous delivery solution for Kubernetes

License:        Apache-2.0
URL:            https://github.com/fluxcd/flux2
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

ExclusiveArch:  x86_64

%description
Flux is a GitOps toolkit and command-line interface for managing continuous
delivery on Kubernetes.

%prep
%autosetup -n flux2-%{version}
go mod download

%build
export GOTOOLCHAIN=local
export CGO_ENABLED=1
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

go build -v \
  -o flux \
  -ldflags "\
    -linkmode=external \
    -compressdwarf=false \
  " \
  ./cmd/flux

%install
install -Dpm0755 flux %{buildroot}%{_bindir}/flux
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
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
* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.8.5-1
- Initial package
