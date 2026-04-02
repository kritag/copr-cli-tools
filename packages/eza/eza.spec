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
Provides:       exa
Obsoletes:      exa < %{version}-%{release}

ExclusiveArch:  x86_64

%description
eza is a modern replacement for ls with sensible defaults, colors, git status,
icons, and tree views.

%prep
%autosetup -n %{name}-%{version}
cargo fetch --locked

%build
cargo build --frozen --release
mkdir -p target/man
pandoc -s -t man man/eza.1.md -o target/man/eza.1
pandoc -s -t man man/eza_colors.5.md -o target/man/eza_colors.5
pandoc -s -t man man/eza_colors-explanation.5.md -o target/man/eza_colors-explanation.5

%install
install -Dpm0755 target/release/eza %{buildroot}%{_bindir}/eza
ln -s eza %{buildroot}%{_bindir}/exa
install -Dpm0644 completions/bash/eza %{buildroot}%{_datadir}/bash-completion/completions/eza
install -Dpm0644 completions/zsh/_eza %{buildroot}%{_datadir}/zsh/site-functions/_eza
install -Dpm0644 completions/fish/eza.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/eza.fish
install -Dpm0644 LICENSE.txt %{buildroot}%{_licensedir}/%{name}/LICENSE.txt
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 target/man/eza.1 %{buildroot}%{_mandir}/man1/eza.1
install -Dpm0644 target/man/eza_colors.5 %{buildroot}%{_mandir}/man5/eza_colors.5
install -Dpm0644 target/man/eza_colors-explanation.5 %{buildroot}%{_mandir}/man5/eza_colors-explanation.5

%files
%{_bindir}/eza
%{_bindir}/exa
%{_datadir}/bash-completion/completions/eza
%{_datadir}/zsh/site-functions/_eza
%{_datadir}/fish/vendor_completions.d/eza.fish
%license %{_licensedir}/%{name}/LICENSE.txt
%doc %{_docdir}/%{name}/README.md
%{_mandir}/man1/eza.1*
%{_mandir}/man5/eza_colors.5*
%{_mandir}/man5/eza_colors-explanation.5*

%changelog
* Thu Mar 26 2025 Codex <codex@example.invalid> - 0.23.4-1
- Initial package
