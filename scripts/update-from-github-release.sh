#!/usr/bin/env bash

set -euo pipefail

usage() {
    echo "Usage: $0 <package>" >&2
    exit 1
}

[[ $# -eq 1 ]] || usage

package="$1"
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
meta_path="${repo_root}/packages/${package}/upstream.env"

if [[ ! -f "${meta_path}" ]]; then
    echo "Missing upstream metadata: ${meta_path}" >&2
    exit 1
fi

# shellcheck disable=SC1090
source "${meta_path}"

: "${UPSTREAM_REPO:?UPSTREAM_REPO is required}"
tag_prefix="${UPSTREAM_TAG_PREFIX:-v}"

api_url="https://api.github.com/repos/${UPSTREAM_REPO}/releases/latest"
tag_name="$(
    curl -fsSL \
        -H "Accept: application/vnd.github+json" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "${api_url}" \
    | jq -r '.tag_name'
)"

if [[ -z "${tag_name}" || "${tag_name}" == "null" ]]; then
    echo "No release tag found for ${UPSTREAM_REPO}" >&2
    exit 1
fi

version="${tag_name}"
if [[ -n "${tag_prefix}" && "${version}" == "${tag_prefix}"* ]]; then
    version="${version#${tag_prefix}}"
fi

"${repo_root}/scripts/bump-version.sh" "${package}" "${version}"
