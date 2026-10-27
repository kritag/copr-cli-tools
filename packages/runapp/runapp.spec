%global debug_package %{nil}

Name:           runapp
Version:        0.5.1
Release:        1%{?dist}
Summary:        Application runner for Linux desktop environments that integrate with systemd

License:        MIT
URL:            https://github.com/c4rlo/runapp
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsystemd)

%description
runapp launches applications in their own systemd scopes or services, for
desktop environments and window managers that integrate with systemd.

%prep
%autosetup

%build
%make_build release native_flag= prefix=%{_prefix}

%install
%make_install prefix=%{_prefix} install_runner=

%files
%license LICENSE*
%doc README.md
%{_bindir}/runapp
%{_mandir}/man1/runapp.1*

%changelog
* Tue Oct 27 2026 Kristian Tagesen <kristian@example.invalid> - 0.5.1-1
- Initial package, adapted from the Arch PKGBUILD
