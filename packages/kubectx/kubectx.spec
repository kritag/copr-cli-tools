Name:           kubectx
Version:        0.9.5
Release:        1%{?dist}
Summary:        Utility to switch between kubectl contexts and namespaces

License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectx
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  grep
Requires:       kubectl
Provides:       kubens = %{version}-%{release}

ExclusiveArch:  x86_64

%description
kubectx provides utilities for switching between kubectl contexts and
Kubernetes namespaces. This package installs both the kubectx and kubens
commands.

%prep
%autosetup -n %{name}-%{version}
rm -f kubectx kubens

export GOPATH="$(pwd)"
go mod download

%build
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOPATH="$(pwd)"
export GOPROXY=off

go build -trimpath -buildmode=pie -mod=readonly -modcacherw \
  -ldflags "\
    -X main.version=%{version} \
    -linkmode external \
    -extldflags \"%{build_ldflags}\" \
    -compressdwarf=false \
  " \
  -v \
  ./cmd/kubectx/...

go build -trimpath -buildmode=pie -mod=readonly -modcacherw \
  -ldflags "\
    -X main.version=%{version} \
    -linkmode external \
    -extldflags \"%{build_ldflags}\" \
    -compressdwarf=false \
  " \
  -v \
  ./cmd/kubens/...

%check
./kubectx --version | grep "%{version}"
./kubens --version | grep "%{version}"

%install
install -Dpm0755 kubectx %{buildroot}%{_bindir}/kubectx
install -Dpm0755 kubens %{buildroot}%{_bindir}/kubens

install -Dpm0644 completion/kubectx.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/kubectx
install -Dpm0644 completion/kubens.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/kubens
install -Dpm0644 completion/_kubectx.zsh \
  %{buildroot}%{_datadir}/zsh/site-functions/_kubectx
install -Dpm0644 completion/_kubens.zsh \
  %{buildroot}%{_datadir}/zsh/site-functions/_kubens
install -Dpm0644 completion/kubectx.fish \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/kubectx.fish
install -Dpm0644 completion/kubens.fish \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/kubens.fish

%files
%{_bindir}/kubectx
%{_bindir}/kubens
%{_datadir}/bash-completion/completions/kubectx
%{_datadir}/bash-completion/completions/kubens
%{_datadir}/zsh/site-functions/_kubectx
%{_datadir}/zsh/site-functions/_kubens
%{_datadir}/fish/vendor_completions.d/kubectx.fish
%{_datadir}/fish/vendor_completions.d/kubens.fish

%changelog
* Wed Mar 26 2026 Codex <codex@example.invalid> - 0.9.5-1
- Initial package
