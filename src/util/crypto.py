import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(data: str, key: str) -> str:
    """
    Salaa annetun datan AES-algoritmilla

    Args:
        data: salattava tieto
        key: salasana, jolla salaus voidaan purkaa
    """
    derived_key = hashlib.sha256(key.encode()).digest()
    iv = os.urandom(16)

    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    padded_data = pad(data.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)

    return (iv + ciphertext).hex()


def decrypt(encrypted_data: str, key: str) -> str:
    """
    Purkaa annetun datan AES-algoritmilla

    Args:
        data: tieto. jonka salaus halutaan purkaa
        key: salasana, jolla salaus voidaan purkaa
    """
    encrypted_bytes = bytes.fromhex(encrypted_data)
    derived_key = hashlib.sha256(key.encode()).digest()
    iv = encrypted_bytes[:16]
    ciphertext = encrypted_bytes[16:]

    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    padded_data = cipher.decrypt(ciphertext)
    data = unpad(padded_data, AES.block_size)

    return data.decode()
