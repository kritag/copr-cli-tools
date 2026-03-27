Name:           kubectl
Version:        1.35.3
Release:        1%{?dist}
Summary:        Kubernetes command-line tool

License:        Apache-2.0
URL:            https://github.com/kubernetes/kubernetes
Source0:        %{url}/archive/refs/tags/v%{version}/kubernetes-%{version}.tar.gz

BuildRequires:  git-core
BuildRequires:  go
BuildRequires:  make
BuildRequires:  rsync

ExclusiveArch:  x86_64

%description
kubectl is the command-line client for Kubernetes clusters.

%prep
%autosetup -n kubernetes-%{version}

%build
export GOTOOLCHAIN=local
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -ldflags=-linkmode=external -ldflags=-compressdwarf=false -modcacherw"
export GOLDFLAGS="-linkmode=external -compressdwarf=false"
export GOPATH="$(pwd)"

make WHAT=cmd/kubectl KUBE_BUILD_PLATFORMS=linux/amd64 KUBE_VERBOSE=5

%install
install -Dpm0755 _output/local/bin/linux/amd64/kubectl %{buildroot}%{_bindir}/kubectl
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
* Wed Mar 26 2026 Codex <codex@example.invalid> - 1.35.3-1
- Build kubectl from the Kubernetes source tree
