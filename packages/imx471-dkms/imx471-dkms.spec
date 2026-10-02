%define debug_package %{nil}

Name:           imx471-dkms
Version:        1.0
Release:        %(git rev-list --count HEAD 2>/dev/null || echo 1).%(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')%{?dist}
Summary:        IMX471 sensor driver via DKMS

License:        GPL-2.0-only
URL:            https://github.com/BenBJD/imx471-dkms
Source0:        https://github.com/BenBJD/imx471-dkms/archive/HEAD.tar.gz

BuildRequires:  git
Requires:       dkms

%description
IMX471 sensor driver for Intel IPU6/IPU7 platforms via DKMS.
This package provides the kernel driver for the Sony IMX471 camera sensor
found in Lenovo ThinkPad X9 and X1 Carbon Gen 14.

%prep
%setup -q -n imx471-dkms-HEAD

%build
# No build needed for DKMS package
true

%install
# Install DKMS module source
install -d %{buildroot}/usr/src/imx471-1.0
cp -a . %{buildroot}/usr/src/imx471-1.0/
rm -rf %{buildroot}/usr/src/imx471-1.0/.git
rm -rf %{buildroot}/usr/src/imx471-1.0/.gitignore

# Install libcamera tuning file if it exists
if [ -f imx471.yaml ]; then
  install -Dm644 imx471.yaml %{buildroot}%{_datadir}/libcamera/ipa/simple/imx471.yaml
fi

%post
# Register with DKMS
dkms add -m imx471 -v 1.0 2>/dev/null || true
dkms build -m imx471 -v 1.0 2>/dev/null || true
dkms install -m imx471 -v 1.0 2>/dev/null || true

%preun
# Unregister from DKMS
dkms remove -m imx471 -v 1.0 --all 2>/dev/null || true

%files
/usr/src/imx471-1.0/
%{_datadir}/libcamera/ipa/simple/imx471.yaml

%changelog
* Thu Oct 02 2024 - 1.0
- Initial Fedora package for IMX471 DKMS module
- Based on BenBJD/imx471-dkms repository
