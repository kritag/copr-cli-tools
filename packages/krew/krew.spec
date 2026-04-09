Name:           krew
Version:        0.5.0
Release:        3%{?dist}
Summary:        Find and install kubectl plugins

License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/krew
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  go
Requires:       git-core
Requires:       kubectl

ExclusiveArch:  x86_64

%description
krew is a plugin manager for kubectl.

%prep
%autosetup -n %{name}-%{version}
GOFLAGS="-mod=readonly" go mod vendor -v

%build
export CGO_LDFLAGS="%{build_ldflags}"
export CGO_CFLAGS="%{build_cflags}"
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CXXFLAGS="%{build_cxxflags}"
export GOFLAGS="-buildmode=pie -mod=vendor -modcacherw"
export GOPATH="$(pwd)"

go build -v \
  -ldflags "\
    -X sigs.k8s.io/krew/internal/version.gitCommit=v%{version} \
    -X sigs.k8s.io/krew/internal/version.gitTag=v%{version} \
    -compressdwarf=false \
    -linkmode=external \
  " \
  -o . \
  ./cmd/...

mv krew kubectl-krew

%check
mkdir -p .test-bin
cat > .test-bin/kubectl <<'EOF'
#!/bin/sh
if [ "$1" = "krew" ]; then
  shift
  exec "$(dirname "$0")/../kubectl-krew" "$@"
fi
echo "unsupported test invocation: kubectl $*" >&2
exit 1
EOF
chmod 0755 .test-bin/kubectl
PATH="$PWD/.test-bin:$PATH" KREW_BINARY="$PWD/kubectl-krew" go test ./...

%install
install -Dpm0755 kubectl-krew %{buildroot}%{_bindir}/kubectl-krew
install -Dpm0755 validate-krew-manifest %{buildroot}%{_bindir}/validate-krew-manifest
install -Dpm0644 README.md %{buildroot}%{_docdir}/%{name}/README.md
cp -a docs %{buildroot}%{_docdir}/%{name}/

%files
%{_bindir}/kubectl-krew
%{_bindir}/validate-krew-manifest
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/docs

%changelog
* Thu Apr 09 2026 Codex <codex@example.invalid> - 0.5.0-3
- Provide a local kubectl shim during tests so integration tests can invoke kubectl krew

* Wed Apr 08 2026 Codex <codex@example.invalid> - 0.5.0-2
- Drop unnecessary kubectl BuildRequires so the package can build before kubectl is present

* Thu Mar 26 2026 Codex <codex@example.invalid> - 0.5.0-1
- Initial package
