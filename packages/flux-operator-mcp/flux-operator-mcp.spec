%global debug_package %{nil}

Name:           flux-operator-mcp
Version:        0.62.1
Release:        1%{?dist}
Summary:        MCP server for debugging Flux CD on live Kubernetes clusters

License:        AGPL-3.0-only
URL:            https://github.com/controlplaneio-fluxcd/flux-operator
Source0:        %{url}/releases/download/v%{version}/flux-operator-mcp_%{version}_linux_amd64.tar.gz

ExclusiveArch:  x86_64

%description
Model Context Protocol server from the Flux Operator project. It lets AI
assistants inspect and debug Flux resources on live clusters. This package
installs the upstream prebuilt binary.

%prep
%autosetup -c -T
tar -xzf %{SOURCE0}

%install
install -Dpm0755 flux-operator-mcp %{buildroot}%{_bindir}/flux-operator-mcp
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/flux-operator-mcp
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Mon Oct 19 2026 kritag <kristian@example.invalid> - 0.61.0-1
- Initial package
