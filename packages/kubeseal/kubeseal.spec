Name:           kubeseal
Version:        0.36.1
Release:        1%{?dist}
Summary:        One-way encrypted Secrets for Kubernetes

License:        Apache-2.0
URL:            https://github.com/bitnami-labs/sealed-secrets
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  go
Requires:       glibc

ExclusiveArch:  x86_64

%description
kubeseal is a client for creating one-way encrypted Kubernetes Secrets for use
with the sealed-secrets controller.

%prep
%autosetup -n sealed-secrets-%{version}

%build
cd cmd/kubeseal

export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

go build -ldflags "-linkmode=external -X=main.VERSION=v%{version}" .

%check
go test ./cmd/kubeseal/... ./pkg/...

%install
install -Dpm0755 cmd/kubeseal/kubeseal %{buildroot}%{_bindir}/kubeseal

%files
%{_bindir}/kubeseal

%changelog
* Wed Mar 26 2026 Codex <codex@example.invalid> - 0.36.1-1
- Initial package
