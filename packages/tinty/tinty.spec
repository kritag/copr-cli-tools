%global commit      bd3aee4361c2c1b94ecffddeaa3780a637bfebef
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tinty
Version:        0.35.0^20261021gitbd3aee4
Release:        1%{?dist}
Summary:        A base16 and base24 color scheme manager

License:        MIT
URL:            https://github.com/tinted-theming/tinty
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  openssl-devel
Requires:       git-core

ExclusiveArch:  x86_64 aarch64

%description
Tinty is a base16 and base24 color scheme manager. This package tracks the
upstream main branch rather than tagged releases.

%prep
%autosetup -n %{name}-%{commit}
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dpm0755 target/release/tinty %{buildroot}%{_bindir}/tinty
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 contrib/completion/tinty.bash %{buildroot}%{_datadir}/bash-completion/completions/tinty
install -Dpm0644 contrib/completion/tinty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/tinty.fish
install -Dpm0644 contrib/completion/tinty.zsh %{buildroot}%{_datadir}/zsh/site-functions/_tinty

%files
%{_bindir}/tinty
%{_datadir}/bash-completion/completions/tinty
%{_datadir}/fish/vendor_completions.d/tinty.fish
%{_datadir}/zsh/site-functions/_tinty
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Mon Oct 12 2026 Kristian Tagesen <kristian@example.invalid> - 0.34.1^20261007git858837c-1
- Initial package, tracking upstream main
