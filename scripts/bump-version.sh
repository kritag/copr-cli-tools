#!/usr/bin/env bash

set -euo pipefail

usage() {
    echo "Usage: $0 <package> <version>" >&2
    exit 1
}

[[ $# -eq 2 ]] || usage

package="$1"
version="$2"

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
spec_path="${repo_root}/packages/${package}/${package}.spec"

if [[ ! -f "${spec_path}" ]]; then
    echo "Spec not found: ${spec_path}" >&2
    exit 1
fi

current_version="$(awk '/^Version:/ {print $2; exit}' "${spec_path}")"

if [[ "${current_version}" == "${version}" ]]; then
    echo "${package}: already at ${version}"
    exit 0
fi

sed -i -E "s/^(Version:[[:space:]]*).*/\1${version}/" "${spec_path}"

echo "${package}: ${current_version} -> ${version}"
