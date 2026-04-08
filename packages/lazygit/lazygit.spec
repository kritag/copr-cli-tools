%global debug_package %{nil}

Name:           lazygit
Version:        0.61.0
Release:        1%{?dist}
Summary:        Simple terminal UI for git commands

License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go

ExclusiveArch:  x86_64

%description
lazygit provides a simple terminal user interface for common git operations.

%prep
%autosetup -n %{name}-%{version}

%build
export CGO_CPPFLAGS="%{optflags}"
export CGO_CFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw -x -v"

go build \
    -ldflags "\
      -linkmode external \
      -extldflags '%{build_ldflags}' \
      -X main.date=$(date --date=@${SOURCE_DATE_EPOCH} -u +%Y-%m-%dT%H:%M:%SZ) \
      -X main.buildSource=binaryRelease \
      -X main.version=%{version} \
      -X main.commit=v%{version} \
    "

%install
install -Dpm0755 lazygit %{buildroot}%{_bindir}/lazygit
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
mkdir -p %{buildroot}%{_docdir}/%{name}
install -pm0644 README*.md %{buildroot}%{_docdir}/%{name}/
cp -r docs/* %{buildroot}%{_docdir}/%{name}/

%files
%{_bindir}/lazygit
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}

%changelog
* Thu Mar 26 2026 Codex <codex@example.invalid> - 0.60.0-1
- Build from source archive
