Name:           tealdeer
Version:        1.9.1
Release:        1%{?dist}
Summary:        Fast tldr client written in Rust

License:        MIT OR Apache-2.0
URL:            https://github.com/tealdeer-rs/tealdeer
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core
Provides:       tldr = %{version}-%{release}
Conflicts:      tldr

ExclusiveArch:  x86_64

%description
tealdeer is a fast client for tldr-pages, community-maintained simplified
help pages for command-line tools. The binary is installed as tldr.

%prep
%autosetup -n %{name}-%{version}
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dpm0755 target/release/tldr %{buildroot}%{_bindir}/tldr
install -Dpm0644 completion/bash_tealdeer %{buildroot}%{_datadir}/bash-completion/completions/tldr
install -Dpm0644 completion/zsh_tealdeer %{buildroot}%{_datadir}/zsh/site-functions/_tldr
install -Dpm0644 completion/fish_tealdeer %{buildroot}%{_datadir}/fish/vendor_completions.d/tldr.fish

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/tldr
%{_datadir}/bash-completion/completions/tldr
%{_datadir}/zsh/site-functions/_tldr
%{_datadir}/fish/vendor_completions.d/tldr.fish

%changelog
* Wed Nov 11 2026 Kristian Tagesen <kristian@example.invalid> - 1.9.1-1
- Initial package
