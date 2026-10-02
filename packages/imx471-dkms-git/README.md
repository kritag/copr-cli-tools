# imx471-dkms

DKMS driver for the Sony IMX471 camera sensor found in Lenovo ThinkPad X9 and X1 Carbon Gen 14 with Intel IPU7.

## Update workflow

1. Check for new commits in the [upstream repository](https://github.com/BenBJD/imx471-dkms)
2. Update the spec file if needed
3. Commit and push
4. Trigger a COPR rebuild for the SCM package

## Notes

- This installs the kernel driver source for automatic compilation via DKMS
- Requires libcamera for full camera functionality
- IPU7 firmware must be installed separately (typically in /lib/firmware/intel/ipu/)
