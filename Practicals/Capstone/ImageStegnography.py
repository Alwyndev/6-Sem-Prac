import tkinter as tk
from tkinter import filedialog, messagebox
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

# GUI Setup
class SteganographyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Steganography")
        self.geometry("500x400")

        # Image path variable
        self.image_path = ""

        # Text input for encoding
        self.text_input_label = tk.Label(self, text="Text to encode:")
        self.text_input_label.pack(pady=10)

        self.text_input = tk.Entry(self, width=40)
        self.text_input.pack(pady=10)

        # Buttons for loading image and saving the encoded image
        self.load_image_button = tk.Button(self, text="Load Image", command=self.load_image)
        self.load_image_button.pack(pady=10)

        self.encode_button = tk.Button(self, text="Encode Text", command=self.encode_image)
        self.encode_button.pack(pady=10)

        self.save_as_copy_button = tk.Button(self, text="Save as Copy", command=self.save_as_copy)
        self.save_as_copy_button.pack(pady=10)

        self.save_button = tk.Button(self, text="Save & Replace Original", command=self.save_image)
        self.save_button.pack(pady=10)

        self.decoded_label = tk.Label(self, text="Decoded Text will appear here", wraplength=400)
        self.decoded_label.pack(pady=10)

    def load_image(self):
        # File dialog to select an image
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            messagebox.showinfo("Image Loaded", f"Image loaded successfully: {self.image_path}")
    
    def encode_image(self):
        text = self.text_input.get()
        if not text or not self.image_path:
            messagebox.showerror("Error", "Please provide text and load an image.")
            return
        
        output_path = "encoded_image.png"  # Default output file
        try:
            encode_text(self.image_path, text, output_path)
            messagebox.showinfo("Success", "Text encoded successfully!")
            self.decode_image(output_path)  # Automatically decode and show text
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def decode_image(self, image_path):
        decoded_text = decode_text(image_path)
        self.decoded_label.config(text=f"Decoded Text: {decoded_text}")

    def save_as_copy(self):
        # Save the encoded image as a new file
        if not self.image_path:
            messagebox.showerror("Error", "Please load an image first.")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            try:
                encode_text(self.image_path, self.text_input.get(), save_path)
                messagebox.showinfo("Success", f"Image saved as copy at {save_path}")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def save_image(self):
        # Save the encoded image, replacing the original image
        if not self.image_path:
            messagebox.showerror("Error", "Please load an image first.")
            return
        
        output_path = self.image_path  # Overwrite original image
        try:
            encode_text(self.image_path, self.text_input.get(), output_path)
            messagebox.showinfo("Success", "Image saved and original replaced!")
            self.decode_image(output_path)  # Automatically decode and show text
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()
