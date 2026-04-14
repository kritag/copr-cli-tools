Name:           kubecolor
Version:        0.6.0
Release:        1%{?dist}
Summary:        Colorize your kubectl output

License:        MIT
URL:            https://github.com/kubecolor/kubecolor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go
Requires:       kubectl

ExclusiveArch:  x86_64

%description
kubecolor colorizes kubectl output to make Kubernetes resources easier to scan.

%prep
%autosetup -n %{name}-%{version}
export GOTOOLCHAIN=auto
go mod download

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export CGO_ENABLED=1
export GOFLAGS="-buildmode=pie -mod=readonly -modcacherw -trimpath"
export GOTOOLCHAIN=auto

go build \
  -ldflags "-compressdwarf=false -linkmode external -extldflags \"%{build_ldflags}\"" \
  .

%install
install -Dpm0755 kubecolor %{buildroot}%{_bindir}/kubecolor
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/kubecolor
%doc %{_docdir}/%{name}/README.md
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 0.6.0-1
- Update to 0.6.0
- Allow automatic Go toolchain bootstrap for Fedora 43
