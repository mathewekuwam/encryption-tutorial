#!/usr/bin/env python3
"""
generate_key.py
Generate a Fernet key and save it to keys/thekey.key (creates keys/ if missing).
This should be run once before encrypting files.
"""

from pathlib import Path
from cryptography.fernet import Fernet
import os

KEY_DIR = Path(__file__).resolve().parents[1] / "keys"
KEY_PATH = KEY_DIR / "thekey.key"

def main():
    KEY_DIR.mkdir(parents=True, exist_ok=True)
    if KEY_PATH.exists():
        print(f"Key already exists at {KEY_PATH}. Remove it first if you want a new key.")
        return

    key = Fernet.generate_key()
    # Save key with restrictive permissions where possible
    with open(KEY_PATH, "wb") as f:
        f.write(key)
    try:
        os.chmod(KEY_PATH, 0o600)
    except Exception:
        # Some systems may not support chmod
        pass
    print(f"Generated key and saved to: {KEY_PATH}")

if __name__ == "__main__":
    main()
