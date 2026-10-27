Name:           dotbot
Version:        1.24.1
Release:        1%{?dist}
Summary:        Tool that bootstraps your dotfiles

License:        MIT
URL:            https://github.com/anishathalye/dotbot
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
Dotbot makes installing your dotfiles as easy as git clone $url && cd dotfiles
&& ./install, even on a freshly installed system. It is driven by a YAML or
JSON config that creates symlinks, directories and shell commands.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dotbot

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/dotbot

%changelog
* Tue Oct 27 2026 Kristian Tagesen <kristian@example.invalid> - 1.24.1-1
- Initial package
