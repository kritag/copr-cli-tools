Name:           zsh-patina
Version:        1.9.0
Release:        1%{?dist}
Summary:        A blazingly fast Zsh syntax highlighter

License:        MIT
URL:            https://github.com/michel-kraemer/zsh-patina
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  git-core

Requires:       gcc-libs

ExclusiveArch:  x86_64 aarch64 armv7hl

%description
zsh-patina is a blazingly fast Zsh plugin that performs syntax highlighting of
your command line while you type.

%prep
%autosetup -p1
cargo fetch --locked

%build
cargo build --frozen --release

%install
install -Dpm0755 target/release/zsh-patina %{buildroot}%{_bindir}/zsh-patina
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md

# Generate and install shell completion
./target/release/zsh-patina completion > _zsh_patina
install -Dpm0644 _zsh_patina %{buildroot}%{_datadir}/zsh/site-functions/_zsh_patina

%files
%{_bindir}/zsh-patina
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_datadir}/zsh/site-functions/_zsh_patina

%changelog
* Fri Aug 15 2026 Kristian Tagesen <kristian.tagesen@tieto.com> - 1.9.0-1
- Initial package, built from source with cargo
