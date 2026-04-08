Name:           bat-extras
Version:        2024.08.24
Release:        1%{?dist}
Summary:        Bash scripts that integrate bat with various command line tools

License:        MIT
URL:            https://github.com/eth-p/bat-extras
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.zip
Source1:        https://raw.githubusercontent.com/eth-p/bat-extras/v%{version}/LICENSE.md
Source2:        https://raw.githubusercontent.com/eth-p/bat-extras/v%{version}/README.md

BuildArch:      noarch
BuildRequires:  unzip
Requires:       bash
Requires:       bat
Requires:       git-core
Requires:       man-db
Requires:       ripgrep

%description
bat-extras provides additional shell utilities that integrate bat with common
command-line workflows.

%prep
%setup -q -T -c -n %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
install -d %{buildroot}%{_bindir}
install -pm0755 bin/* %{buildroot}%{_bindir}/

install -d %{buildroot}%{_docdir}/%{name}
install -pm0644 doc/* %{buildroot}%{_docdir}/%{name}/
install -pm0644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.md

install -d %{buildroot}%{_mandir}/man1
install -pm0644 man/*.1 %{buildroot}%{_mandir}/man1/

install -Dpm0644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE.md

%files
%{_bindir}/bat-modules
%{_bindir}/batdiff
%{_bindir}/batgrep
%{_bindir}/batman
%{_bindir}/batpipe
%{_bindir}/batwatch
%{_bindir}/prettybat
%doc %{_docdir}/%{name}
%license %{_licensedir}/%{name}/LICENSE.md
%{_mandir}/man1/*.1*

%changelog
* Wed Apr 08 2026 Codex <codex@example.invalid> - 2024.08.24-1
- Initial package
