from unittest import TestCase
from util.crypto import encrypt, decrypt


class TestCrypto(TestCase):
    def test_encrypt_data_can_be_encrypted(self):
        data = "testing data"
        key = "testing key"
        encrypted = encrypt(data, key)
        self.assertIsInstance(encrypted, str)

    def test_decrypt_returns_original_data(self):
        data = "some secret message"
        key = "supersecretkey"
        encrypted = encrypt(data, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, data)

    def test_decrypt_with_wrong_key_raises(self):
        data = "another secret"
        key = "correctkey"
        wrong_key = "wrongkey"
        encrypted = encrypt(data, key)
        with self.assertRaises(ValueError):
            decrypt(encrypted, wrong_key)
