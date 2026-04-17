Name:           yq
Version:        4.53.2
Release:        1%{?dist}
Summary:        Portable YAML, JSON, XML, CSV, and TOML processor

License:        MIT
URL:            https://github.com/mikefarah/yq
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  zstd

ExclusiveArch:  x86_64 aarch64

%description
yq is a lightweight command-line processor for YAML, JSON, XML, CSV, and TOML
documents.

%prep
%autosetup -p1
go mod vendor

%build
export CGO_CPPFLAGS="%{optflags}"
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
go build .

%install
install -Dpm0755 yq %{buildroot}%{_bindir}/yq
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
./yq shell-completion bash > yq.bash
install -Dpm0644 yq.bash %{buildroot}%{_datadir}/bash-completion/completions/yq
./yq shell-completion zsh > _yq
install -Dpm0644 _yq %{buildroot}%{_datadir}/zsh/site-functions/_yq
./yq shell-completion fish > yq.fish
install -Dpm0644 yq.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/yq.fish

%files
%{_bindir}/yq
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_datadir}/bash-completion/completions/yq
%{_datadir}/zsh/site-functions/_yq
%{_datadir}/fish/vendor_completions.d/yq.fish

%changelog
* Wed Mar 25 2026 Codex <codex@example.invalid> - 4.52.4-1
- Build from source archive and install shell completions
