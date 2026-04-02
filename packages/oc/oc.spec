%global debug_package %{nil}

Name:           oc
Version:        4.21.7
Release:        1%{?dist}
Summary:        OpenShift command-line client

License:        Apache-2.0
URL:            https://github.com/openshift/oc
Source0:        https://mirror.openshift.com/pub/openshift-v4/clients/ocp/%{version}/openshift-client-linux.tar.gz

Provides:       oc
Conflicts:      origin-client origin-client-bin

ExclusiveArch:  x86_64

%description
oc is the command-line client for OpenShift clusters. This package installs
the upstream prebuilt binary.

%prep
%setup -c -T
tar xzf %{SOURCE0}

%build

%install
install -Dpm0755 oc %{buildroot}%{_bindir}/oc
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/oc completion bash > %{buildroot}%{_datadir}/bash-completion/completions/oc
%{buildroot}%{_bindir}/oc completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_oc

%files
%{_bindir}/oc
%{_datadir}/bash-completion/completions/oc
%{_datadir}/zsh/site-functions/_oc

%changelog
* Thu Mar 27 2025 Codex <codex@example.invalid> - 4.21.7-1
- Initial package
