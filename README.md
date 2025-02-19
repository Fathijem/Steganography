# Secure Data Hiding in Images using Steganography
## 🔒 Project Overview
This project implements **steganography-based encryption and decryption** that hides a **secret message within an image** using **password protection**. The message is stored in the **blue channel** of pixel values, keeping the image visually unchanged.

With this system, only users who enter the **correct password** can extract the hidden message, making it a **secure communication tool**.

## ✨ Features
✅ **Secure Message Hiding** – Encrypts text inside an image using pixel manipulation.  
✅ **Password-Protected Access** – Only users with the correct password can decrypt the message.  
✅ **Lossless Storage (PNG Format Recommended)** – Prevents corruption due to compression.  
✅ **Error Handling & Validation** – Ensures message integrity and prevents unauthorized access.  

---

## ⚙️ **Installation & Requirements**
### **🔹 Prerequisites**
- Python 3.x
- Pip
- OpenCV (`cv2`) for image processing

### **🔹 Install Dependencies**
If pip is not install, install pip using the following command:
```sh
python -m pip install --upgrade pip
```

Run the following command to install OpenCV:
```sh
pip install opencv-python
```
## 🚀 **Usage**
### **Encryption (encrypt.py)**
1. Run the script:
```sh
python encrypt.py
```
If you're using IDE click on Run -> Run Module

2. Enter:
The image filename (e.g., mypic.png).
The secret message to hide.
A password for secure decryption.
The encrypted image (encrypted_image.png) will be saved.

### **Decryption (decrypt.py)**
1. Run the script:
```sh
python decrypt.py
```
If you're using IDE click on Run -> Run Module

2. Enter:
The encrypted image filename (encrypted_image.png).
The correct password.
If authenticated, the hidden message will be revealed.

## 🛠️ **Example**
### **Encryption**
```sh
Enter image filename (e.g., mypic.png): sample.png
Enter secret message: Hello, this is a secret!
Enter a passcode: 1234
✅ Encryption completed! Encrypted image saved as 'encrypted_image.png'.
```
### **Decryption**
```sh
Enter encrypted image filename (e.g., encrypted_image.png): encrypted_image.png
Enter passcode for decryption: 1234
🔓 Decrypted Message: Hello, this is a secret!
```
