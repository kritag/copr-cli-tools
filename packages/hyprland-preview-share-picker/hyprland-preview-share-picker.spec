Name:           hyprland-preview-share-picker
Version:        0.2.1
Release:        1%{?dist}
Summary:        Alternative share picker for Hyprland with window and monitor previews

License:        MIT
URL:            https://github.com/WhySoBad/hyprland-preview-share-picker
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Submodule: hyprwm/hyprland-protocols v0.6.4 (pinned with main source)
Source1:        https://github.com/hyprwm/hyprland-protocols/archive/refs/tags/v0.6.4.tar.gz#/hyprland-protocols-0.6.4.tar.gz

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)

Requires:       gtk4
Requires:       gtk4-layer-shell
Requires:       xdg-desktop-portal-hyprland
Requires:       hyprland
Suggests:       slurp

ExclusiveArch:  x86_64

%description
An alternative share picker for Hyprland with window and monitor previews.
Provides a graphical interface for selecting windows and monitors when sharing
your screen through XDG desktop portals.

%prep
%autosetup -n %{name}-%{version}
# Populate the git submodule (lib/hyprland-protocols) from the bundled tarball
mkdir -p lib/hyprland-protocols
tar -xzf %{SOURCE1} -C lib/hyprland-protocols --strip-components=1
cargo fetch --locked

%build
export CARGO_TARGET_DIR=target
cargo build --frozen --release
./target/release/%{name} schema > schema.json

%install
install -Dpm0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 schema.json %{buildroot}%{_datadir}/%{name}/schema.json
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/schema.json
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed May 27 2026 Kristian Tagesen <kristian.tagesen@tieto.com> - 0.2.1-1
- Initial package
