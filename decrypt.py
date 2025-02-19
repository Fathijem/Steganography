import cv2
image_path = input("Enter encrypted image filename (e.g., encrypted_image.png): ")
img = cv2.imread(image_path)
if img is None:
    print("❌ Error: Unable to load image. Check the file path and try again.")
    exit()
msg_length = int.from_bytes([img[0, i, 0] for i in range(4)], byteorder="big")
full_msg = ""
idx = 0
found_null = False  
for i in range(1, img.shape[0]): 
    for j in range(img.shape[1]):
        if idx < msg_length:
            char_code = img[i, j, 0]
            if char_code == 0: 
                found_null = True
                break
            full_msg += chr(char_code)
            idx += 1
        else:
            break
    if idx >= msg_length or found_null:
        break  
full_msg = full_msg.split("\0")[0]  
if "|" not in full_msg:
    print("❌ Error: Incorrect or corrupted data in image.")
    exit()
stored_password, secret_message = full_msg.split("|", 1)
password = input("Enter passcode for decryption: ")
if password != stored_password:
    print("❌ Incorrect password! Access denied.")
    exit()

print("🔓 Decrypted Message:", secret_message)






