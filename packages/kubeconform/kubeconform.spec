Name:           kubeconform
Version:        0.7.0
Release:        1%{?dist}
Summary:        Fast Kubernetes manifests validator with Custom Resource support

License:        Apache-2.0
URL:            https://github.com/yannh/kubeconform
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git-core
BuildRequires:  go
Requires:       glibc

ExclusiveArch:  x86_64

%description
kubeconform validates Kubernetes manifests against upstream JSON schemas and
supports Custom Resources.

%prep
%autosetup -n %{name}-%{version}
go mod download

%build
cd cmd/%{name}
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

go build -ldflags "-w -s -linkmode=external" .

%check
go test ./...

%install
install -Dpm0755 cmd/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 Readme.md %{buildroot}%{_docdir}/%{name}/Readme.md
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/%{name}
%doc %{_docdir}/%{name}/Readme.md
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 0.7.0-1
- Initial package
