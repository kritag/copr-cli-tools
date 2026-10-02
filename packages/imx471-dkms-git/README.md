# imx471-dkms-git

DKMS build of the Sony IMX471 camera sensor driver (Lenovo ThinkPad X9 /
X1 Carbon Gen 14, Intel IPU7), from a pinned commit of
[BenBJD/imx471-dkms](https://github.com/BenBJD/imx471-dkms).

Builds three modules, because the stock kernel lacks IMX471 support in all
three places:

| Module | Why |
| --- | --- |
| `imx471` | the sensor driver, not yet upstream |
| `ipu-bridge` | stock kernel module has no IMX471 entry |
| `intel_skl_int3472_discrete` | sensor power rails and privacy LED |

Installing only `imx471` is not enough: the driver probes, finds nothing
powered on the I2C bus and fails with `-EIO`.

## Update workflow

Upstream publishes no releases, so `upstream.env` is intentionally empty
and `scripts/update-from-github-release.sh` skips this package. To bump:

1. `git ls-remote https://github.com/BenBJD/imx471-dkms HEAD` for the new SHA
2. Update `%global commit` and `%global snapdate` in the spec
3. Add a `%changelog` entry, commit and push

## Notes

- `intel_skl_int3472_discrete` is built from a kernel-version subdirectory
  (`6.18`–`7.2`). A kernel newer than the newest subdirectory will fail to
  build until upstream adds one.
- Conflicts with `imx471-intel-dkms`; remove any hand-registered
  `imx471-intel` DKMS module first.
- Targets libcamera's software ISP, not the proprietary IPU7 stack. The
  IPU7 firmware (`/lib/firmware/intel/ipu/ipu7_fw.bin`) is not shipped here.
