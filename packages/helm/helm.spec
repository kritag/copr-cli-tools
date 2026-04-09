Name:           helm
Version:        4.1.4
Release:        1%{?dist}
Summary:        Kubernetes package manager

License:        Apache-2.0
URL:            https://github.com/helm/helm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go

ExclusiveArch:  x86_64

%description
Helm is a package manager for Kubernetes.

%prep
%autosetup -n %{name}-%{version}
GOFLAGS="-mod=readonly" go mod vendor -v

%build
export CGO_LDFLAGS="%{build_ldflags}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_CPPFLAGS="${CPPFLAGS}"
export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"

go build -v \
  -ldflags "\
    -compressdwarf=false \
    -linkmode=external \
    -X helm.sh/helm/v4/internal/version.version=v%{version} \
    -X helm.sh/helm/v4/internal/version.gitCommit=v%{version} \
  " \
  ./cmd/helm

%install
install -Dpm0755 helm %{buildroot}%{_bindir}/helm
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
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
* Wed Mar 26 2026 Codex <codex@example.invalid> - 4.1.3-1
- Initial package
