Name:           flavours
Version:        0.7.1
Release:        1%{?dist}
Summary:        CLI to build and use base16 schemes

License:        MIT
URL:            https://github.com/Misterio77/flavours
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Requires:       git

ExclusiveArch:  x86_64

%description
flavours is a simple and easy CLI to build and use base16 schemes.

%prep
%autosetup -n %{name}-%{version}
cargo fetch --locked

%build
cargo build --frozen --release
target/release/flavours --completions bash > flavours.bash
target/release/flavours --completions fish > flavours.fish
target/release/flavours --completions zsh > _flavours

%install
install -Dpm0755 target/release/flavours %{buildroot}%{_bindir}/flavours
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 example.toml %{buildroot}%{_sysconfdir}/%{name}.conf
install -Dpm0644 flavours.bash %{buildroot}%{_datadir}/bash-completion/completions/flavours
install -Dpm0644 flavours.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/flavours.fish
install -Dpm0644 _flavours %{buildroot}%{_datadir}/zsh/site-functions/_flavours

%files
%{_bindir}/flavours
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_datadir}/bash-completion/completions/flavours
%{_datadir}/fish/vendor_completions.d/flavours.fish
%{_datadir}/zsh/site-functions/_flavours
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 0.7.1-1
- Initial package
