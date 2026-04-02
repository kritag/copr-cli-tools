Name:           sops
Version:        3.12.2
Release:        1%{?dist}
Summary:        Editor of encrypted files for YAML, JSON, ENV, INI, and binary formats

License:        MPL-2.0
URL:            https://github.com/getsops/sops
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        bash_autocomplete
Source2:        zsh_autocomplete

BuildRequires:  git-core
BuildRequires:  go
Requires:       glibc

ExclusiveArch:  x86_64

%description
sops is an editor for encrypted files that supports YAML, JSON, ENV, INI, and
binary formats.

%prep
%autosetup -n %{name}-%{version}

go mod download

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOPROXY=off

go build \
  -trimpath \
  -buildmode=pie \
  -mod=readonly \
  -modcacherw \
  -ldflags "-linkmode=external -extldflags \"%{build_ldflags}\"" \
  ./cmd/sops

%check
go test

%install
install -Dpm0644 %{_sourcedir}/%{SOURCE1} \
  %{buildroot}%{_datadir}/bash-completion/completions/sops
install -Dpm0644 %{_sourcedir}/%{SOURCE2} \
  %{buildroot}%{_datadir}/zsh/site-functions/_sops
install -Dpm0755 sops %{buildroot}%{_bindir}/sops
install -Dpm0644 README.rst %{buildroot}%{_docdir}/%{name}/README.rst

%files
%{_bindir}/sops
%{_datadir}/bash-completion/completions/sops
%{_datadir}/zsh/site-functions/_sops
%doc %{_docdir}/%{name}/README.rst

%changelog
* Wed Mar 26 2025 Codex <codex@example.invalid> - 3.12.2-1
- Initial package
