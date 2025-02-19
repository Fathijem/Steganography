import cv2
import os
image_path = input("Enter image filename (e.g., mypic.png): ")
img = cv2.imread(image_path)
if img is None:
    print("❌ Error: Unable to load image. Check the file path and try again.")
    exit()
height, width, _ = img.shape
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
full_msg = password + "|" + msg + "\0"  
msg_length = len(full_msg)
if msg_length > height * width:
    print("❌ Error: Message is too long for this image!")
    exit()
msg_bytes = msg_length.to_bytes(4, byteorder="big")
for i in range(4):
    img[0, i, 0] = msg_bytes[i]
idx = 0
for i in range(1, height):  
    for j in range(width):
        if idx < msg_length:
            img[i, j, 0] = ord(full_msg[idx])  
            idx += 1
        else:
            break
    if idx >= msg_length:
        break
output_image = "encrypted_image.png"
cv2.imwrite(output_image, img)
os.system(f"start {output_image}") 
print(f"✅ Encryption completed! Encrypted image saved as '{output_image}'.")
