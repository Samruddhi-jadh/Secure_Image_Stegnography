import cv2
import numpy as np

def load_image(image_path):
    """Loads an image from the given path."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or unsupported format.")
    return img

def save_image(image, output_path):
    """Saves an image to the specified path."""
    cv2.imwrite(output_path, image)

def convert_text_to_binary(text):
    """Converts a string into its binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def convert_binary_to_text(binary_data):
    """Converts binary data back into a string."""
    byte_chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(byte, 2)) for byte in byte_chunks if int(byte, 2) != 0)

def get_image_size(image):
    """Returns the dimensions of the image."""
    return image.shape[:2]
