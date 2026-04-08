Name:           lesspipe
Version:        2.24
Release:        2%{?dist}
Summary:        Input filter for the pager less

License:        GPL-2.0-or-later
URL:            https://www-zeuthen.desy.de/~friebel/unix/lesspipe.html
Source0:        https://github.com/wofr06/lesspipe/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        lesspipe.sh

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  make
BuildRequires:  zsh
Requires:       bash
Requires:       less

%description
lesspipe enhances less by preprocessing many non-plain-text input formats so
they can be inspected directly in the pager.

This package installs the upstream lesspipe implementation in a private path so
it can be used on Fedora systems without conflicting with files shipped by the
less and less-color packages.

%prep
%autosetup -n %{name}-%{version}

%build
./configure \
  --prefix=%{_prefix} \
  --bindir=%{_libexecdir}/%{name} \
  --libexecdir=%{_libexecdir}/%{name} \
  --mandir=%{_datadir}/%{name}/man/man1 \
  --bash-completion-dir=%{_datadir}/bash-completion/completions \
  --zsh-completion-dir=%{_datadir}/zsh/site-functions
make

%install
make DESTDIR=%{buildroot} install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/lesspipe.sh
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_libexecdir}/%{name}/archive_color
%{_libexecdir}/%{name}/lesspipe.sh
%{_libexecdir}/%{name}/lesscomplete
%{_sysconfdir}/profile.d/lesspipe.sh
%{_datadir}/%{name}/man/man1/lesspipe.1*
%{_datadir}/bash-completion/completions/less
%{_datadir}/zsh/site-functions/_less
%doc %{_docdir}/%{name}/README.md
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.24-2
- Install upstream lesspipe in a private path to avoid Fedora file conflicts

* Wed Apr 08 2026 Codex <codex@example.invalid> - 2.24-1
- Initial package
