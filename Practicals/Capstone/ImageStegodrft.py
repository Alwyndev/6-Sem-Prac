from PIL import Image
import numpy as np

def encode_text(image_path, text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = np.array(img, dtype=np.uint8)

    # Convert message length to a 32-bit binary string
    length_bin = format(len(text), '032b')
    # Convert text to binary
    text_bin = ''.join(format(ord(i), '08b') for i in text)
    # Combine the length and the text
    binary_text = length_bin + text_bin
    
    idx = 0
    rows, cols, channels = data.shape
    total_pixels = rows * cols * channels

    if len(binary_text) > total_pixels:
        raise ValueError("The image is too small to encode this message.")

    for i in range(rows):
        for j in range(cols):
            for k in range(3):  # For each RGB channel
                if idx < len(binary_text):
                    data[i, j, k] = (data[i, j, k] & ~1) | int(binary_text[idx])
                    idx += 1

    encoded_img = Image.fromarray(data)
    encoded_img.save(output_path)
    print("Text encoded successfully!")

def decode_text(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = np.array(img, dtype=np.uint8)
    
    binary_text = ""
    rows, cols, channels = data.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                binary_text += str(data[i, j, k] & 1)

    # First 32 bits represent the length of the message
    length_bin = binary_text[:32]
    message_length = int(length_bin, 2)

    message = ""
    for i in range(message_length):
        start = 32 + i * 8
        byte = binary_text[start:start+8]
        message += chr(int(byte, 2))

    print("Text Decoded Successfully!")
    return message

# Example usage:
encode_text("encoded_image.png", input("Enter the text to hide in the image:  "), "output.png")
print(f'Secret Message:  {decode_text("output.png")}')