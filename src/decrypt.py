#!/usr/bin/env python3
"""
decrypt.py
Decrypts .enc files inside the 'examples/' directory using the key at keys/thekey.key.
By default it writes a .dec file (original filename without .enc) and leaves the .enc file intact.
"""

from pathlib import Path
from cryptography.fernet import Fernet
import sys

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"
KEY_PATH = ROOT / "keys" / "thekey.key"

def load_key():
    if not KEY_PATH.exists():
        print(f"Key not found at {KEY_PATH}. Run generate_key.py or place your key at {KEY_PATH}.")
        sys.exit(1)
    return KEY_PATH.read_bytes()

def find_encrypted_files():
    return [p for p in EXAMPLES_DIR.iterdir() if p.is_file() and p.name.endswith(".enc")]

def decrypt_file(path: Path, fernet: Fernet):
    token = path.read_bytes()
    data = fernet.decrypt(token)
    # restore original name by removing the added '.enc' suffix
    orig_name = path.name[:-4]  # remove '.enc'
    out_path = path.with_name(orig_name + ".dec")
    out_path.write_bytes(data)
    return out_path

def main():
    if not EXAMPLES_DIR.exists():
        print(f"No examples/ directory found at {EXAMPLES_DIR}.")
        sys.exit(1)

    key = load_key()
    f = Fernet(key)
    enc_files = find_encrypted_files()
    if not enc_files:
        print("No .enc files found in examples/.")
        return

    print("Encrypted files found:")
    for p in enc_files:
        print(" -", p.name)

    confirm = input("Proceed to decrypt these files? (yes/no): ").strip().lower()
    if confirm not in ("yes", "y"):
        print("Aborting.")
        return

    for p in enc_files:
        try:
            out = decrypt_file(p, f)
            print(f"Decrypted {p} -> {out}")
        except Exception as e:
            print(f"Failed to decrypt {p}: {e}")

    print("\nDone. Encrypted files (.enc) were left in place. You can remove .enc files after verifying the decrypted outputs.")

if __name__ == "__main__":
    main()
