Name:           oh-my-posh
Version:        29.9.2
Release:        1%{?dist}
Summary:        A prompt theme engine for any shell

License:        MIT
URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  go

Requires:       glibc

ExclusiveArch:  x86_64

%description
oh-my-posh is a prompt theme engine for any shell.

%prep
%autosetup -n %{name}-%{version}

cd src
go mod download

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"

cd src
go build \
  -ldflags "-linkmode=external \
    -X github.com/jandedobbeleer/oh-my-posh/src/build.Version=%{version} \
    -X github.com/jandedobbeleer/oh-my-posh/src/build.Date=%(date +%%F)" \
  -o %{name}

%install
cd src
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 ../COPYING %{buildroot}%{_licensedir}/%{name}/LICENSE
install -dm0755 %{buildroot}%{_datadir}/%{name}/themes
install -pm0644 ../themes/* %{buildroot}%{_datadir}/%{name}/themes/

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/themes/
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Fri Mar 27 2026 Codex <codex@example.invalid> - 29.9.2-1
- Initial package
