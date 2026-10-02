%global commit      0fd3c09f9654b3cb79454975d40efdf68ca5b4dd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate    20261002

%global dkmsname    imx471
%global dkmsver     1.0

%global debug_package %{nil}

Name:           imx471-dkms-git
Version:        1.0
Release:        1.%{snapdate}git%{shortcommit}%{?dist}
Summary:        Sony IMX471 camera sensor driver for Intel IPU7, via DKMS

License:        GPL-2.0-only
URL:            https://github.com/BenBJD/imx471-dkms
Source0:        %{url}/archive/%{commit}/imx471-dkms-%{commit}.tar.gz

BuildArch:      noarch

Requires:       dkms
Requires:       gcc
Requires:       make
Requires:       kernel-devel

Provides:       imx471-dkms = %{version}-%{release}
Conflicts:      imx471-intel-dkms

%description
Out-of-tree DKMS build of the Sony IMX471 camera sensor driver found on
Lenovo ThinkPad X9 and X1 Carbon Gen 14 (Intel IPU7).

Builds three modules, since the stock kernel lacks IMX471 support in all
three places:
  * imx471                       - the sensor driver itself
  * ipu-bridge                   - patched to recognise the IMX471
  * intel_skl_int3472_discrete   - sensor power rails and privacy LED

Without the latter two the sensor driver probes and fails with -EIO,
because nothing powers the sensor or wires it to the IPU.

Intended for use with libcamera's software ISP rather than the
proprietary IPU7 userspace stack. A libcamera tuning file is installed
to %{_datadir}/libcamera/ipa/simple/imx471.yaml.

%prep
%autosetup -n imx471-dkms-%{commit}

%build
# Nothing is compiled at RPM build time; DKMS builds against the
# running kernel at install time.

%install
install -d %{buildroot}%{_usrsrc}/%{dkmsname}-%{dkmsver}
cp -a . %{buildroot}%{_usrsrc}/%{dkmsname}-%{dkmsver}/
rm -rf %{buildroot}%{_usrsrc}/%{dkmsname}-%{dkmsver}/.git*

install -Dpm 0644 imx471.yaml \
    %{buildroot}%{_datadir}/libcamera/ipa/simple/imx471.yaml

%post
if [ "$1" -ge 1 ]; then
    dkms add     -m %{dkmsname} -v %{dkmsver} --rpm_safe_upgrade || :
    dkms build   -m %{dkmsname} -v %{dkmsver} || :
    dkms install -m %{dkmsname} -v %{dkmsver} --force || :
fi

%preun
if [ "$1" -eq 0 ]; then
    dkms remove -m %{dkmsname} -v %{dkmsver} --all --rpm_safe_upgrade || :
fi

%files
%license LICENSE
%doc README.md
%{_usrsrc}/%{dkmsname}-%{dkmsver}/
%{_datadir}/libcamera/ipa/simple/imx471.yaml

%changelog
* Fri Oct 02 2026 kritag - 1.0-1.20261002git0fd3c09
- Initial package, git snapshot 0fd3c09
