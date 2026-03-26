Name:           eza
Version:        0.23.4
Release:        1%{?dist}
Summary:        Modern replacement for ls

License:        EUPL-1.2
URL:            https://github.com/eza-community/eza
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  pandoc

ExclusiveArch:  x86_64

%description
eza is a modern replacement for ls with sensible defaults, colors, git status,
icons, and tree views.

%prep
%autosetup -n %{name}-%{version}
cargo fetch --locked

%build
cargo build --frozen --release
pandoc -s -t man man/eza.1.md -o eza.1

%install
install -Dpm0755 target/release/eza %{buildroot}%{_bindir}/eza
install -Dpm0644 LICENCE %{buildroot}%{_licensedir}/%{name}/LICENCE
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 eza.1 %{buildroot}%{_mandir}/man1/eza.1

%files
%{_bindir}/eza
%license %{_licensedir}/%{name}/LICENCE
%doc %{_docdir}/%{name}/README.md
%{_mandir}/man1/eza.1*

%changelog
* Thu Mar 26 2026 Codex <codex@example.invalid> - 0.23.4-1
- Initial package
