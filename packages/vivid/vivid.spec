Name:           vivid
Version:        0.10.1
Release:        1%{?dist}
Summary:        LS_COLORS manager with multiple themes

License:        Apache-2.0 AND MIT
URL:            https://github.com/sharkdp/vivid
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core

ExclusiveArch:  x86_64

%description
vivid is an LS_COLORS manager that lets you generate a color theme for your
terminal file listings. It ships with multiple built-in themes.

%prep
%autosetup -p1
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dpm0755 target/release/vivid %{buildroot}%{_bindir}/vivid
install -Dpm0644 LICENSE-APACHE %{buildroot}%{_licensedir}/%{name}/LICENSE-APACHE
install -Dpm0644 LICENSE-MIT %{buildroot}%{_licensedir}/%{name}/LICENSE-MIT
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md

%files
%{_bindir}/vivid
%license %{_licensedir}/%{name}/LICENSE-APACHE
%license %{_licensedir}/%{name}/LICENSE-MIT
%doc %{_docdir}/%{name}/README.md

%changelog
* Fri Mar 28 2026 kritag <3776749+kritag@users.noreply.github.com> - 0.10.1-1
- Initial package
