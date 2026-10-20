#!/usr/bin/python3
"""Append a snippet to one file inside an asar, in place: patch-asar.py ASAR INNER_PATH SNIPPET_FILE"""
import json, struct, sys

asar, inner, snippet = sys.argv[1:4]
extra = open(snippet, "rb").read()

def pad4(n):
    return (n + 3) & ~3

with open(asar, "rb") as f:
    raw = f.read()
hsize = struct.unpack_from("<I", raw, 4)[0]
jlen = struct.unpack_from("<I", raw, 12)[0]
header = json.loads(raw[16:16 + jlen])
data = raw[8 + hsize:]

node = header
for part in inner.split("/"):
    node = node["files"][part]
assert "offset" in node, f"{inner} is not a packed file"
start = int(node["offset"])
body = data[start:start + node["size"]] + extra
node["offset"] = str(len(data))
node["size"] = len(body)
node.pop("integrity", None)

j = json.dumps(header, separators=(",", ":")).encode()
hpay = struct.pack("<I", len(j)) + j + b"\0" * (pad4(len(j)) - len(j))
out = struct.pack("<II", 4, len(hpay) + 4) + struct.pack("<I", len(hpay)) + hpay + data + body
open(asar, "wb").write(out)
