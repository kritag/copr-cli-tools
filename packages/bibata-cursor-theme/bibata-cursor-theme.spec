%global theme_name Bibata-Modern-Classic

Name:           bibata-cursor-theme
Version:        2.0.7
Release:        1%{?dist}
Summary:        Material based cursor theme (Bibata Modern Classic)

License:        GPL-3.0-or-later
URL:            https://github.com/ful1e5/Bibata_Cursor
Source0:        %{url}/releases/download/v%{version}/%{theme_name}.tar.xz

BuildArch:      noarch

%description
Bibata material based cursor theme package.

This package intentionally ships only the `Bibata-Modern-Classic` theme,
which matches GNOME cursor-theme setting `Bibata-Modern-Classic`.

%prep
%setup -q -n %{theme_name}

%build
# Nothing to build.

%install
install -dm0755 %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}/

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Apr 15 2026 Codex <codex@example.invalid> - 2.0.7-1
- Initial package shipping only Bibata-Modern-Classic
