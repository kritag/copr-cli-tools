# QML submodules pinned to the commits referenced by the v%%{version} tag.
# The GitHub release tarball ships these as empty directories, so they are
# fetched separately. Refresh both when bumping Version (see README.md).
%global quill_commit    bc13deae669a1333a0d7bdd991c7015270a16a38
%global icons_commit    10db5facf6a560e60d2693ccd1909267ef436002

Name:           hyprfm
Version:        0.6.1
Release:        1%{?dist}
Summary:        A lightweight Qt6/QML file manager for Hyprland

License:        MIT
URL:            https://github.com/soyeb-jim285/hyprfm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/soyeb-jim285/quill/archive/%{quill_commit}.tar.gz#/quill-%{quill_commit}.tar.gz
Source2:        https://github.com/soyeb-jim285/quill-icons/archive/%{icons_commit}.tar.gz#/quill-icons-%{icons_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  kf6-kwindowsystem-devel

# Loaded at runtime rather than linked, so not caught by automatic deps
Requires:       qt6-qtwayland
Requires:       gvfs
Requires:       xdg-utils

Recommends:     wl-clipboard
Recommends:     fd-find
Recommends:     udisks2
Recommends:     poppler-utils
Recommends:     perl-Image-ExifTool
Suggests:       bat
Suggests:       ffmpeg-free
Suggests:       gvfs-smb
Suggests:       gvfs-mtp

ExclusiveArch:  x86_64 aarch64

%description
HyprFM is a lightweight Qt6/QML file manager built for Hyprland. It provides
tabbed browsing, file previews, and sidebar device management.

%prep
%autosetup -n %{name}-%{version}
# Populate the empty submodule directories left by the release tarball
tar -xzf %{SOURCE1} --strip-components=1 -C src/qml/Quill
tar -xzf %{SOURCE2} --strip-components=1 -C src/qml/icons

%build
cmake -B build -S . -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_TESTS=OFF \
    -DHYPRFM_DATA_DIR=%{_datadir}/%{name}
cmake --build build --parallel

%install
install -Dpm0755 build/src/%{name} %{buildroot}%{_bindir}/%{name}

# Themes and QML sources are resolved at runtime under HYPRFM_DATA_DIR
install -dm0755 %{buildroot}%{_datadir}/%{name}/themes
install -pm0644 themes/*.toml %{buildroot}%{_datadir}/%{name}/themes/
install -Dpm0644 build/src/HyprFM/qmldir %{buildroot}%{_datadir}/%{name}/HyprFM/qmldir
if [ -f build/src/HyprFM/hyprfm.qmltypes ]; then
    install -Dpm0644 build/src/HyprFM/hyprfm.qmltypes \
        %{buildroot}%{_datadir}/%{name}/HyprFM/hyprfm.qmltypes
fi
install -dm0755 %{buildroot}%{_datadir}/%{name}/src
cp -a src/qml %{buildroot}%{_datadir}/%{name}/src/qml

install -Dpm0644 dist/io.github.soyeb_jim285.HyprFM.desktop \
    %{buildroot}%{_datadir}/applications/io.github.soyeb_jim285.HyprFM.desktop
install -Dpm0644 dist/io.github.soyeb_jim285.HyprFM.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.github.soyeb_jim285.HyprFM.svg
install -Dpm0644 dist/io.github.soyeb_jim285.HyprFM.metainfo.xml \
    %{buildroot}%{_metainfodir}/io.github.soyeb_jim285.HyprFM.metainfo.xml
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/io.github.soyeb_jim285.HyprFM.desktop
%{_datadir}/icons/hicolor/scalable/apps/io.github.soyeb_jim285.HyprFM.svg
%{_metainfodir}/io.github.soyeb_jim285.HyprFM.metainfo.xml
%license %{_licensedir}/%{name}/LICENSE
%doc README.md

%changelog
* Sat Aug 15 2026 Kristian Tagesen <kristian@example.invalid> - 0.6.1-1
- Initial package, built from source with cmake
