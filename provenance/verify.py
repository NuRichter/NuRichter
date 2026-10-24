"""
Verify that this diary is the original, signed work of NuRichter.

    pip install cryptography
    python provenance/verify.py

Checks:
  1. manifest.sig is a valid Ed25519 signature over manifest.json, made by
     the key whose fingerprint is published in the README footer.
  2. every file listed in manifest.json still has the signed SHA-256 hash.
"""
import base64
import hashlib
import json
import sys
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
EXPECTED_FINGERPRINT = (HERE / "FINGERPRINT").read_text().strip()


def main():
    body = (HERE / "manifest.json").read_bytes()
    sig = base64.b64decode((HERE / "manifest.sig").read_text().strip())
    manifest = json.loads(body)
    pub_raw = base64.b64decode(manifest["public_key_ed25519"])
    fp = hashlib.sha256(pub_raw).hexdigest()[:16].upper()
    if fp != EXPECTED_FINGERPRINT:
        sys.exit(f"✗ key fingerprint {fp} is not NuRichter's ({EXPECTED_FINGERPRINT})")
    try:
        Ed25519PublicKey.from_public_bytes(pub_raw).verify(sig, body)
    except InvalidSignature:
        sys.exit("✗ signature does not match manifest.json")
    bad = [f for f, h in manifest["files"].items()
           if not (REPO / f).exists() or hashlib.sha256((REPO / f).read_bytes()).hexdigest() != h]
    if bad:
        sys.exit("✗ modified or missing since signing:\n  " + "\n  ".join(bad))
    print(f"✓ {len(manifest['files'])} files verified · signed by NuRichter · key {fp}")


if __name__ == "__main__":
    main()
