Name:           protonplus
Version:        0.6.8
Release:        1%{?dist}
Summary:        Modern compatibility tools manager for Steam and other game launchers

License:        GPL-3.0-only
URL:            https://github.com/Vysp3r/ProtonPlus
Source0:        %{url}/archive/v%{version}/ProtonPlus-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 1.0.0
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sdl3) >= 3.2.0

%description
ProtonPlus is a GTK4/libadwaita manager for compatibility tools such as
Proton-GE, Wine and DXVK for Steam, Lutris, Heroic, Bottles and other game
launchers.

%prep
%autosetup -n ProtonPlus-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.vysp3r.ProtonPlus

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.vysp3r.ProtonPlus.desktop

%files -f com.vysp3r.ProtonPlus.lang
%license LICENSE.md
%doc README.md
%{_bindir}/protonplus
%{_datadir}/applications/com.vysp3r.ProtonPlus.desktop
%{_datadir}/glib-2.0/schemas/com.vysp3r.ProtonPlus.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.vysp3r.ProtonPlus*
%{_datadir}/metainfo/com.vysp3r.ProtonPlus.metainfo.xml

%changelog
* Wed Nov 11 2026 Kristian Tagesen <kristian@example.invalid> - 0.6.8-1
- Initial package
