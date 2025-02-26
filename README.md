## 🖼️ Secure Data Hiding in Images using Steganography  

A Python-based **steganography tool** that allows **secure embedding and extraction of hidden messages** inside images using **encryption and LSB (Least Significant Bit) encoding**. Includes **a Streamlit-powered GUI** for easy interaction.  


## ✨ Features  
✅ **Hide Encrypted Messages** – Embed encrypted text into images using **LSB steganography**.  
✅ **Extract Hidden Messages** – Decode and decrypt the secret message from the stego-image.  
✅ **AES Encryption (Optional)** – Encrypt messages before embedding for added security.  
✅ **Streamlit GUI** – A simple web-based UI for encoding and decoding.  
✅ **Command-Line Interface (CLI)** – Supports **CLI-based embedding and extraction**.  
✅ **Lightweight & Open Source** – Easy to install, modify, and use.  



## 🏗️ Technologies Used 🚀
- **Python** – Core programming language  
- **OpenCV** – Image processing and manipulation  
- **Cryptography (AES)** – Secure encryption and decryption  
- **Streamlit** – GUI for user-friendly interaction  
- **NumPy** – Efficient image data handling  



## 📥 Installation Guide
### 🔹 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 2️⃣ Run the Application
```bash
streamlit run app.py
```



## 🔍 **How It Works?** 🚀

### **1️⃣ Encoding Process (Hiding Data in Image)**  
1. The user uploads an image (`.jpg` or `.png`).  
2. The secret message is **converted to binary** and optionally encrypted.  
3. The binary data is embedded into the **Least Significant Bit (LSB)** of the image pixels.  
4. A **stego-image** is generated, visually identical to the original.  

### **2️⃣ Decoding Process (Extracting Hidden Message)**  
1. The user uploads the **stego-image**.  
2. The application extracts **hidden binary data** from the image pixels.  
3. It identifies the **end marker** to determine where the message ends.  
4. If encrypted, the message is **decrypted** and displayed.  

### **3️⃣ Download Process**  
1. After embedding, the stego-image is **generated and displayed**.  
2. The user clicks **"Download Encrypted Image"** to save it.  
3. The image is stored in the **Download/** folder or a chosen location.  
4. The downloaded image appears **unaltered** but contains hidden data.  


## 🔐 **Security Measures**  
1. **Password Protection** – Messages can be encrypted with a password before embedding, ensuring only authorized users can decrypt them.  
2. **Stealth Mode** – Without the correct key, the image appears completely normal, preventing detection.  
3. **End Marker** – A predefined **end marker** ensures no extra data is extracted beyond the hidden message.  
4. **LSB Manipulation** – Embedding in the **Least Significant Bit (LSB)** minimizes distortion, making modifications imperceptible.


## 📜 **License**  
This project is **open-source** and available for use, modification.

## **"🔒 Secure your secrets with invisible encryption! Try image steganography today! 🚀🖼️"**  
