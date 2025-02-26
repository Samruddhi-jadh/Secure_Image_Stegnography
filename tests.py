import unittest
import utils
import crypto_graphy
from cryptography.fernet import Fernet

class TestSteganography(unittest.TestCase):
    
    def test_text_to_binary_conversion(self):
        text = "Hello"
        binary = utils.convert_text_to_binary(text)
        expected_binary = "0100100001100101011011000110110001101111"
        self.assertEqual(binary, expected_binary)
    
    def test_binary_to_text_conversion(self):
        binary = "0100100001100101011011000110110001101111"
        text = utils.convert_binary_to_text(binary)
        expected_text = "Hello"
        self.assertEqual(text, expected_text)
    
    def test_encryption_decryption(self):
        key = Fernet.generate_key()
        cipher = Fernet(key)
        message = "Secret Message"
        encrypted_message = cipher.encrypt(message.encode())
        decrypted_message = cipher.decrypt(encrypted_message).decode()
        self.assertEqual(decrypted_message, message)
    
if __name__ == '__main__':
    unittest.main()
