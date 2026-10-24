# provenance · proof this diary is the original

The text, lettering and layout of [NuRichter's profile](https://github.com/NuRichter) are
original work, drawn by hand-picked type and signed (the two blended illustrations
belong to their artists). Anyone can check it; nobody else can forge it.

| layer | what it proves | how to check |
|---|---|---|
| **Ed25519 signature** | every file (README, LICENSE, all artwork) was published by the holder of NuRichter's private key and hasn't been modified since | `pip install cryptography && python provenance/verify.py` |
| **Key fingerprint** | which key is NuRichter's. It's pinned in git history since the first signed release and in the README source | compare with [`FINGERPRINT`](FINGERPRINT) |
| **OpenTimestamps** | `manifest.json` existed at a given moment, anchored in the Bitcoin blockchain, so it predates any copy | `pip install opentimestamps-client && ots verify provenance/manifest.json.ots` |
| **Sigstore attestation** | GitHub Actions in *this* repository attested the files; the entry sits in a public append-only transparency log | `gh attestation verify assets/diary/dark/hero.svg -R NuRichter/NuRichter` |
| **Sealed letter** | `letter.sealed` is AES-256-GCM (key derived with scrypt). Only its author can open it | — |

Copies of this profile are reported weekly by the *Clone Finder* workflow and
removed through GitHub's DMCA process. See [LICENSE](../LICENSE).
