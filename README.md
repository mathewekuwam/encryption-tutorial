# Encryption Tutorial — Safe Educational Example

**Purpose:** educational demonstration of using `cryptography.Fernet` to encrypt/decrypt files in a safe, non-destructive way.  
**Not for malicious use.** Do not use this project to encrypt systems you do not own or control. The author disclaims responsibility for misuse.

## What this repo contains
- `src/generate_key.py` — generate a Fernet key and save to `keys/thekey.key`
- `src/encrypt.py` — encrypts files in `examples/` and produces `.enc` files (keeps originals by default)
- `src/decrypt.py` — decrypts `.enc` files in `examples/` and writes `.dec` files (keeps `.enc` files)
- `examples/` — add test files here (e.g., `sample.txt`)
- `.gitignore` — keeps keys out of git

## Getting started (local)
1. Clone the repo and `cd` into it.
2. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
