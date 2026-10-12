Name:           papirus-folders
Version:        1.14.0
Release:        1%{?dist}
Summary:        Change the folder color in the Papirus icon theme

License:        MIT
URL:            https://github.com/PapirusDevelopmentTeam/papirus-folders
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
Requires:       bash
Requires:       papirus-icon-theme

%description
papirus-folders is a script that changes the color of folders in the Papirus
icon theme.

%prep
%autosetup

%build

%install
%make_install PREFIX=%{_prefix} ZSHCOMPDIR=%{_datadir}/zsh/site-functions

%files
%license LICENSE
%doc README.md
%{_bindir}/papirus-folders
%{_datadir}/bash-completion/completions/papirus-folders
%{_datadir}/zsh/site-functions/_papirus-folders

%changelog
* Mon Oct 12 2026 Kristian Tagesen <kristian@example.invalid> - 1.14.0-1
- Initial package
