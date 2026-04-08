%global debug_package %{nil}

Name:           oh-my-posh
Version:        29.9.2
Release:        2%{?dist}
Summary:        A prompt theme engine for any shell

License:        MIT
URL:            https://github.com/JanDeDobbeleer/oh-my-posh
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/posh-linux-amd64

Requires:       glibc

ExclusiveArch:  x86_64

%description
oh-my-posh is a prompt theme engine for any shell.

%prep
%autosetup -n %{name}-%{version}

%install
install -Dpm0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 COPYING %{buildroot}%{_licensedir}/%{name}/LICENSE
install -dm0755 %{buildroot}%{_datadir}/%{name}/themes
install -pm0644 themes/* %{buildroot}%{_datadir}/%{name}/themes/

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/themes/
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 29.9.2-2
- Repackage upstream release binary instead of building from source
- Keep bundled theme files from the source archive

* Fri Mar 27 2026 Codex <codex@example.invalid> - 29.9.2-1
- Initial package
