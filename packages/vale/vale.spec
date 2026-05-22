%global debug_package %{nil}

Name:           vale
Version:        3.14.2
Release:        1%{?dist}
Summary:        A linter for prose

License:        MIT
URL:            https://github.com/vale-cli/vale
Source0:        %{url}/releases/download/v%{version}/vale_%{version}_Linux_64-bit.tar.gz

ExclusiveArch:  x86_64

%description
Vale is a command-line tool that brings code-like linting to prose. It is
syntax-aware and supports multiple markup formats (Markdown, AsciiDoc,
reStructuredText, HTML, and more) as well as many writing styles.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 vale %{buildroot}%{_bindir}/vale
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/vale
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Thu May 22 2025 Kristian Tagesen <kristian.tagesen@tieto.com> - 3.14.2-1
- Initial package
