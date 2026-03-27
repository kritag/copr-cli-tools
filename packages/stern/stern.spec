Name:           stern
Version:        1.33.1
Release:        1%{?dist}
Summary:        Multi pod and container log tailing for Kubernetes

License:        Apache-2.0
URL:            https://github.com/stern/stern
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  go
Requires:       glibc

ExclusiveArch:  x86_64

%description
stern tails logs from multiple Kubernetes pods and containers.

%prep
%autosetup -n %{name}-%{version}
GOFLAGS="-mod=readonly" go mod vendor -v

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"
export GOPATH="$(pwd)"

go build -v -x \
  -ldflags "\
    -compressdwarf=false \
    -linkmode=external \
    -X github.com/stern/stern/cmd.version=%{version} \
  " \
  -o ./out/%{name}

%check
go test -v ./...

%install
install -Dpm0755 ./out/%{name} %{buildroot}%{_bindir}/%{name}

%{buildroot}%{_bindir}/%{name} --completion=bash > stern.bash
%{buildroot}%{_bindir}/%{name} --completion=fish > stern.fish
%{buildroot}%{_bindir}/%{name} --completion=zsh > _stern

install -Dpm0644 stern.bash \
  %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm0644 stern.fish \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dpm0644 _stern \
  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dpm0644 *.md -t %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}
%doc %{_docdir}/%{name}

%changelog
* Wed Mar 26 2026 Codex <codex@example.invalid> - 1.33.1-1
- Initial package
