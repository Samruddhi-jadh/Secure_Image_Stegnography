from cryptography.fernet import Fernet
import base64
import os
import hashlib
from getpass import getpass  # For password input

# Generate a key from a password
def generate_key(password: str, salt: bytes = None):
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt if not provided
        with open("salt.key", "wb") as salt_file:
            salt_file.write(salt)  # Store the salt for later use
    else:
        with open("salt.key", "rb") as salt_file:
            salt = salt_file.read()

    # Derive a 256-bit key from the password using PBKDF2
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.urlsafe_b64encode(key[:32])  # Ensure compatibility with Fernet

# Encrypt message
def encrypt_message(message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

if __name__ == "__main__":
    password = getpass("Enter encryption password: ")  # Secure password input
    secret_text = "Confidential Data"
    
    # Encryption
    encrypted_text = encrypt_message(secret_text, password)
    print("\nEncrypted:", encrypted_text)
    
    # Decryption
    password_verify = getpass("\nEnter decryption password: ")  # Ask for the password again
    try:
        decrypted_text = decrypt_message(encrypted_text, password_verify)
        print("Decrypted:", decrypted_text)
    except Exception as e:
        print("Decryption failed! Incorrect password or corrupted data.")
