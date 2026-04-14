Name:           terraform
Version:        1.14.8
Release:        1%{?dist}
Summary:        Build and update infrastructure as code idempotently

License:        BUSL-1.1
URL:            https://github.com/hashicorp/terraform
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        terraform.bash
Source2:        terraform.zsh

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go
BuildRequires:  bash-completion
BuildRequires:  zsh
Requires:       glibc
Recommends:     diffutils
Provides:       terragrunt-iac-provider

ExclusiveArch:  x86_64

%description
Terraform is a HashiCorp tool for building and updating infrastructure as
code idempotently.

%prep
%autosetup -n %{name}-%{version}
go mod download

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export CGO_LDFLAGS="%{build_ldflags}"
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
export GOPROXY=off

go build \
  -o terraform-binary \
  -ldflags "-linkmode=external -extldflags \"%{build_ldflags}\" -X github.com/hashicorp/terraform/version.dev=no" \
  .

%install
install -Dpm0644 %{SOURCE1} \
  %{buildroot}%{_datadir}/bash-completion/completions/terraform
install -Dpm0644 %{SOURCE2} \
  %{buildroot}%{_datadir}/zsh/site-functions/_terraform
install -Dpm0755 terraform-binary %{buildroot}%{_bindir}/terraform
install -Dpm0644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/terraform
%{_datadir}/bash-completion/completions/terraform
%{_datadir}/zsh/site-functions/_terraform
%license %{_licensedir}/%{name}/LICENSE

%changelog
* Tue Apr 14 2026 Codex <codex@example.invalid> - 1.14.8-1
- Initial package
