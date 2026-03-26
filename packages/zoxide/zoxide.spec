Name:           zoxide
Version:        0.9.9
Release:        1%{?dist}
Summary:        Smarter cd command for the shell

License:        MIT
URL:            https://github.com/ajeetdsouza/zoxide
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core

ExclusiveArch:  x86_64

%description
zoxide is a smarter cd command that remembers which directories you use most
frequently and lets you jump to them quickly.

%prep
%autosetup -p1
cargo fetch --locked

%build
cargo build --frozen --release --all-features

%install
install -Dpm0755 target/release/zoxide %{buildroot}%{_bindir}/zoxide
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/
install -Dpm0644 contrib/completions/_zoxide %{buildroot}%{_datadir}/zsh/site-functions/_zoxide
install -Dpm0644 contrib/completions/zoxide.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/zoxide.fish
install -Dpm0644 contrib/completions/zoxide.nu %{buildroot}%{_datadir}/nushell/vendor/autoload/zoxide.nu
install -Dpm0644 contrib/completions/zoxide.bash %{buildroot}%{_datadir}/bash-completion/completions/zoxide

%files
%{_bindir}/zoxide
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_mandir}/man1/*.1*
%{_datadir}/zsh/site-functions/_zoxide
%{_datadir}/fish/vendor_completions.d/zoxide.fish
%{_datadir}/nushell/vendor/autoload/zoxide.nu
%{_datadir}/bash-completion/completions/zoxide

%changelog
* Wed Mar 25 2026 Codex <codex@example.invalid> - 0.9.9-1
- Build from source and install docs, man pages, and completions
