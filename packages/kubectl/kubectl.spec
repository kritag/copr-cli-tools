Name:           kubectl
Version:        1.36.0
Release:        1%{?dist}
Summary:        Kubernetes command-line tool

License:        Apache-2.0
URL:            https://github.com/kubernetes/kubernetes
Source0:        %{url}/archive/refs/tags/v%{version}/kubernetes-%{version}.tar.gz

BuildRequires:  git-core
BuildRequires:  go

ExclusiveArch:  x86_64

%description
kubectl is the command-line client for Kubernetes clusters.

%prep
%autosetup -n kubernetes-%{version}

%build
export GOTOOLCHAIN=local
# Fedora 43 ships Go 1.25, but Kubernetes 1.36's go.work requires 1.26.
# Disable workspace mode so Go uses module mode from the main go.mod instead.
export GOWORK=off
export CGO_ENABLED=1
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"

go build -v \
  -o kubectl \
  -ldflags "\
    -linkmode=external \
    -compressdwarf=false \
    -X k8s.io/client-go/pkg/version.gitVersion=v%{version} \
    -X k8s.io/component-base/version.gitVersion=v%{version} \
    -X k8s.io/client-go/pkg/version.gitMajor=1 \
    -X k8s.io/component-base/version.gitMajor=1 \
    -X k8s.io/client-go/pkg/version.gitMinor=35 \
    -X k8s.io/component-base/version.gitMinor=35 \
    -X k8s.io/client-go/pkg/version.gitTreeState=archive \
    -X k8s.io/component-base/version.gitTreeState=archive \
  " \
  ./cmd/kubectl

%install
install -Dpm0755 kubectl %{buildroot}%{_bindir}/kubectl
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/kubectl completion bash > %{buildroot}%{_datadir}/bash-completion/completions/kubectl
%{buildroot}%{_bindir}/kubectl completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_kubectl
%{buildroot}%{_bindir}/kubectl completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/kubectl.fish

%files
%{_bindir}/kubectl
%{_datadir}/bash-completion/completions/kubectl
%{_datadir}/zsh/site-functions/_kubectl
%{_datadir}/fish/vendor_completions.d/kubectl.fish
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Fri Apr 24 2026 Codex <codex@example.invalid> - 1.35.4-1
- Disable Go workspace mode during build for Fedora 43 compatibility

* Thu Mar 26 2026 Codex <codex@example.invalid> - 1.35.3-1
- Build kubectl from the Kubernetes source tree
