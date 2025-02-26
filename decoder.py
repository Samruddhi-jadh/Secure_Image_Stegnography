import cv2
import hashlib
import os
from cryptography.fernet import Fernet

# Load encryption key
def load_key():
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Encryption key file 'key.key' not found.")
    
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Hash the password (used for verification)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()[:16]  # 16-char hash

# Decrypt the message using Fernet
def decrypt_message(encrypted_message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

# Extract hidden data from an image (Fixed)
def extract_data(image, password):
    binary_msg = ""
    for row in image:
        for pixel in row:
            for i in range(3):
                binary_msg += str(pixel[i] & 1)

    # Stop at the end-of-message delimiter
    delimiter = '1111111111111110'
    end_index = binary_msg.find(delimiter)
    if end_index != -1:
        binary_msg = binary_msg[:end_index]

    # Convert binary to text
    chars = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    extracted_data = "".join(chr(int(c, 2)) for c in chars)

    # Extract stored password hash and message
    stored_password_hash = extracted_data[:16]  # Extract the first 16 characters (hash)
    hidden_message = extracted_data[17:] if len(extracted_data) > 17 else ""  # Extract the actual message

    # Verify password
    if stored_password_hash == hash_password(password):
        return hidden_message
    else:
        return "⚠️ Incorrect Password! Image contains no visible message."
