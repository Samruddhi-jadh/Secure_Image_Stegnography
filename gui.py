import streamlit as st
import numpy as np
import cv2
import os
from encoder import hide_data
from decoder import extract_data

st.title("🖼️ Secure Image Steganography")

# Sidebar option
option = st.sidebar.selectbox("Choose an action:", ["Hide Data", "Extract Data"])

# Hide Data
if option == "Hide Data":
    st.header("🔐 Encrypt Message into Image")
    uploaded_image = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg", "jfif"])
    secret_message = st.text_area("📝 Enter secret message:")
    password = st.text_input("🔑 Set a password:", type="password")

    if st.button("Hide Data 🔒"):
        if uploaded_image and secret_message and password:
            try:
                # Convert uploaded file to OpenCV format
                file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
                image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

                if image is None:
                    st.error("❌ Invalid image format! Please upload a valid image.")
                else:
                    # Encrypt and hide data in the image
                    encrypted_image = hide_data(image, secret_message,password)

                    if encrypted_image is not None:
                        # Save encrypted image
                        encrypted_image_path = "encrypted_image.png"
                        cv2.imwrite(encrypted_image_path, encrypted_image)

                        # Display Encrypted Image
                        st.image(encrypted_image, caption="Encrypted Image (Appears Normal)", channels="BGR")

                        # Download Button
                        with open(encrypted_image_path, "rb") as file:
                            st.download_button("⬇️ Download Encrypted Image", file.read(), "encrypted_image.png", "image/png")

                        st.success("✅ Data successfully hidden in the image!")
                    else:
                        st.error("❌ Failed to hide data in the image.")
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")

# Extract Data
elif option == "Extract Data":
    st.header("🗝️ Decrypt Message from Image")
    uploaded_file = st.file_uploader("📥 Upload a stego-image", type=["png", "jpg", "jpeg", "jfif"])
    password = st.text_input("🔑 Enter the decryption password:", type="password")

    if uploaded_file and password:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        encrypted_img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        # Decrypt message
        hidden_msg = extract_data(encrypted_img, password)
        st.success(f"Decrypted Message: {hidden_msg}")

