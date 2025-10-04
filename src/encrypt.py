#!/usr/bin/env python3
"""
encrypt.py
Encrypts files inside the 'examples/' directory using a Fernet key stored at keys/thekey.key.
By default it creates .enc files and keeps original files (non-destructive).
"""

from pathlib import Path
from cryptography.fernet import Fernet
import sys

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
KEY_PATH = ROOT / "keys" / "thekey.key"

def load_key():
    if not KEY_PATH.exists():
        print(f"Key not found at {KEY_PATH}. Run generate_key.py first.")
        sys.exit(1)
    return KEY_PATH.read_bytes()

def find_files_to_encrypt():
    files = []
    for p in EXAMPLES_DIR.iterdir():
        if p.is_file() and not p.name.endswith(".enc") and p.name != KEY_PATH.name:
            files.append(p)
    return files

def encrypt_file(path: Path, fernet: Fernet):
    data = path.read_bytes()
    token = fernet.encrypt(data)
    out_path = path.with_suffix(path.suffix + ".enc")
    out_path.write_bytes(token)
    return out_path

def main():
    if not EXAMPLES_DIR.exists():
        print(f"No examples/ directory found at {EXAMPLES_DIR}. Create it and add files to test.")
        sys.exit(1)

    key = load_key()
    f = Fernet(key)
    to_encrypt = find_files_to_encrypt()
    if not to_encrypt:
        print("No files to encrypt in examples/ (skipping).")
        return

    print("Files to encrypt:")
    for p in to_encrypt:
        print(" -", p.name)

    confirm = input("Proceed to encrypt these files? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Aborting.")
        return

    for p in to_encrypt:
        out = encrypt_file(p, f)
        print(f"Encrypted {p} -> {out}")

    print("\nDone. Originals were kept. If you want to securely remove originals, do so manually.")
    print("Key is at:", KEY_PATH)
    print("IMPORTANT: keep that key safe. Without it you cannot decrypt files.")

if __name__ == "__main__":
    main()
