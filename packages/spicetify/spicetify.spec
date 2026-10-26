%global debug_package %{nil}
%global __strip /bin/true

Name:           spicetify
Version:        2.46.4
Release:        1%{?dist}
Summary:        Command-line tool to customize the Spotify client

License:        LGPL-2.1-only
URL:            https://github.com/spicetify/cli
Source0:        %{url}/releases/download/v%{version}/spicetify-%{version}-linux-amd64.tar.gz
Source1:        https://raw.githubusercontent.com/spicetify/cli/v%{version}/LICENSE
Source2:        https://raw.githubusercontent.com/spicetify/cli/v%{version}/README.md

ExclusiveArch:  x86_64

%description
spicetify customizes the Spotify desktop client with themes, extensions and
custom apps. The binary looks up its bundled Themes, Extensions, CustomApps and
jsHelper directories next to the real executable, so everything is installed
under %{_datadir}/%{name} and %{_bindir}/spicetify is a symlink.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -dm0755 %{buildroot}%{_datadir}/%{name}
cp -a CustomApps Extensions Themes jsHelper css-map.json globals.d.ts \
    %{buildroot}%{_datadir}/%{name}/
install -pm0755 spicetify %{buildroot}%{_datadir}/%{name}/spicetify
install -dm0755 %{buildroot}%{_bindir}
ln -s ../share/%{name}/spicetify %{buildroot}%{_bindir}/spicetify
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.md

%files
%{_bindir}/spicetify
%{_datadir}/%{name}
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md

%changelog
* Mon Oct 26 2026 Kristian Tagesen <kristian@example.invalid> - 2.46.4-1
- Initial package from upstream Linux amd64 release tarball
