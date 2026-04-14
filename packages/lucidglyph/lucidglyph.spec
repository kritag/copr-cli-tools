Name:           lucidglyph
Version:        0.14.0
Release:        1%{?dist}
Summary:        Tuned font rendering adjustments for Linux

License:        GPL-3.0-only
URL:            https://github.com/maximilionus/lucidglyph
Source0:        %{url}/archive/refs/tags/v%{version}.zip#/%{name}-%{version}.zip

BuildArch:      noarch
BuildRequires:  unzip
Requires:       fontconfig
Requires:       freetype2
Requires:       pam

%description
lucidglyph provides carefully tuned adjustments designed to improve font
rendering on Linux systems.

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build; package ships configuration files.

%install
install -dm0755 %{buildroot}%{_sysconfdir}/fonts/conf.d
find src/modules/fontconfig -type f -print0 | while IFS= read -r -d '' f; do
  install -pm0644 "$f" %{buildroot}%{_sysconfdir}/fonts/conf.d/
done

install -dm0755 %{buildroot}%{_sysconfdir}/environment.d
find src/modules/environment -type f -print0 | while IFS= read -r -d '' f; do
  install -pm0644 "$f" %{buildroot}%{_sysconfdir}/environment.d/
done

%files
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*
%config(noreplace) %{_sysconfdir}/environment.d/*

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 0.14.0-1
- Initial package
