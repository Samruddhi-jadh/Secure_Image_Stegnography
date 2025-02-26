import argparse
import os
from cryptography.fernet import Fernet
from encoder import encode_data
from decoder import decode_data

# Load or generate encryption key
def load_key():
    key_path = "key.key"
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    with open(key_path, "rb") as key_file:
        return key_file.read()

# Encrypt message
def encrypt_message(message, key):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

def main():
    parser = argparse.ArgumentParser(description="Secure Data Hiding in Image Using Steganography")
    parser.add_argument("-e", "--embed", help="Message to embed in image", type=str)
    parser.add_argument("-i", "--image", help="Path to input image", required=True)
    parser.add_argument("-o", "--output", help="Path to save stego-image", default="output/stego.png")
    parser.add_argument("-d", "--decode", help="Extract hidden message from stego-image", action="store_true")
    parser.add_argument("-k", "--key", help="Encryption key file (optional)", type=str)

    args = parser.parse_args()

    # Load encryption key
    if args.key:
        if not os.path.exists(args.key):
            print(f"[ERROR] Key file '{args.key}' not found!")
            return
        with open(args.key, "rb") as key_file:
            key = key_file.read()
    else:
        key = load_key()

    if args.embed:
        print("[INFO] Embedding message into image...")
        encrypted_message = encrypt_message(args.embed, key)
        encode_data(args.image, encrypted_message)  # Function handles file paths
        print(f"[SUCCESS] Stego-image saved at {args.output}")

    elif args.decode:
        print("[INFO] Extracting hidden message from stego-image...")
        hidden_data = decode_data(args.image)  # Function handles file paths
        decrypted_message = decrypt_message(hidden_data, key)
        print(f"[SUCCESS] Hidden message: {decrypted_message}")

    else:
        print("[ERROR] No operation specified. Use -e to embed or -d to decode.")
        parser.print_help()

if __name__ == "__main__":
    main()
