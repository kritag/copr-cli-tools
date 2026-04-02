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

update_from_openshift_mirror() {
    local mirror_url latest_url latest_html version

    mirror_url="${UPSTREAM_MIRROR_URL%/}"
    latest_url="${mirror_url}/latest/"
    latest_html="$(
        curl -fsSL "${latest_url}"
    )"

    version="$(
        printf '%s\n' "${latest_html}" \
        | grep -oE 'openshift-client-linux-[0-9][^"/]*\.tar\.gz' \
        | sed -E 's/^openshift-client-linux-//; s/\.tar\.gz$//' \
        | sort -V \
        | tail -n1
    )"

    if [[ -z "${version}" ]]; then
        echo "No OpenShift client version found at ${latest_url}" >&2
        exit 1
    fi

    "${repo_root}/scripts/bump-version.sh" "${package}" "${version}"
}

if [[ ! -f "${meta_path}" ]]; then
    echo "Missing upstream metadata: ${meta_path}" >&2
    exit 1
fi

# shellcheck disable=SC1090
source "${meta_path}"

if [[ -z "${UPSTREAM_REPO:-}" && -n "${OWNER:-}" && -n "${REPO:-}" ]]; then
    UPSTREAM_REPO="${OWNER}/${REPO}"
fi

if [[ -n "${UPSTREAM_MIRROR_URL:-}" ]]; then
    update_from_openshift_mirror
    exit 0
fi

if [[ -z "${UPSTREAM_REPO:-}" ]]; then
    echo "Skipping ${package}: no supported upstream release metadata" >&2
    exit 0
fi

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
