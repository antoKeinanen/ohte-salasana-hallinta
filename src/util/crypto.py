import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data: str, key: str) -> str:
    derived_key = hashlib.sha256(key.encode()).digest()
    iv = os.urandom(16)

    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    padded_data = pad(data.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)

    return (iv + ciphertext).hex()


def decrypt(encrypted_data: str, key: str) -> str:
    encrypted_bytes = bytes.fromhex(encrypted_data)
    derived_key = hashlib.sha256(key.encode()).digest()
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]

    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    padded_data = cipher.decrypt(ciphertext)
    data = unpad(padded_data, AES.block_size)

    return data.decode()
