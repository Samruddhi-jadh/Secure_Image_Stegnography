import cv2
import numpy as np
import os
from cryptography.fernet import Fernet

# Generate and save an encryption key if not found
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Encrypt the message
def encrypt_message(message):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Hide encrypted data in an image (Fix: Accepts an image array instead of a file path)
def hide_data(image, secret_message,password):
    generate_key()  # Ensure key is available
    encrypted_message = encrypt_message(secret_message)

    # Convert encrypted message to binary
    binary_data = ''.join(format(byte, '08b') for byte in encrypted_message)
    binary_data += '1111111111111110'  # End marker

    if image is None:
        raise ValueError("Invalid image input. Ensure a valid image is provided.")

    img = image.copy()  # Work on a copy of the image
    height, width, _ = img.shape
    data_index = 0
    data_length = len(binary_data)

    for row in range(height):
        for col in range(width):
            pixel = img[row, col]
            for channel in range(3):  
                if data_index < data_length:
                    pixel[channel] = (pixel[channel] & 254) | int(binary_data[data_index])
                    data_index += 1
                else:
                    break
            img[row, col] = pixel
            if data_index >= data_length:
                break
        if data_index >= data_length:
            break

    return img  # Return the modified image instead of saving it directly
