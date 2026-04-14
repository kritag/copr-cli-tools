%global debug_package %{nil}

Name:           vivid
Version:        0.11.1
Release:        2%{?dist}
Summary:        LS_COLORS manager with multiple themes

License:        Apache-2.0 AND MIT
URL:            https://github.com/sharkdp/vivid
Source0:        %{url}/releases/download/v%{version}/vivid-v%{version}-x86_64-unknown-linux-gnu.tar.gz
Source1:        https://raw.githubusercontent.com/sharkdp/vivid/v%{version}/LICENSE-APACHE
Source2:        https://raw.githubusercontent.com/sharkdp/vivid/v%{version}/LICENSE-MIT
Source3:        https://raw.githubusercontent.com/sharkdp/vivid/v%{version}/README.md

ExclusiveArch:  x86_64

%description
vivid is an LS_COLORS manager that lets you generate a color theme for your
terminal file listings. It ships with multiple built-in themes.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
VIVID_BIN="$(find . -maxdepth 2 -type f -name vivid | head -n1)"
test -n "${VIVID_BIN}"
install -Dpm0755 "${VIVID_BIN}" %{buildroot}%{_bindir}/vivid
install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE-APACHE
install -Dpm0644 %{SOURCE2} %{buildroot}%{_licensedir}/%{name}/LICENSE-MIT
install -Dpm0644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}/README.md

%files
%{_bindir}/vivid
%license %{_licensedir}/%{name}/LICENSE-APACHE
%license %{_licensedir}/%{name}/LICENSE-MIT
%doc %{_docdir}/%{name}/README.md

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 0.11.1-2
- Repackage upstream release binary instead of building from source

* Sat Mar 28 2026 kritag <3776749+kritag@users.noreply.github.com> - 0.10.1-1
- Initial package
