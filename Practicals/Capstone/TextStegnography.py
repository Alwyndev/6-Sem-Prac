def encode_text_in_file(file_path, secret_message):
    with open(file_path, "r", encoding="utf-8") as file:
        cover_text = file.read()
    
    message_bytes = secret_message.encode('utf-8')
    message_length = len(message_bytes)
    
    header = format(message_length, '032b')
    message_bin = ''.join(format(byte, '08b') for byte in message_bytes)
    full_bits = header + message_bin
    
    encoded_tokens = [(" " if bit == '0' else "  ") for bit in full_bits]
    encoded_str = "\u200b".join(encoded_tokens)  
    
    stego_text = cover_text.rstrip() + "\n" + encoded_str  

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(stego_text)
    
    print("Message hidden successfully!")

def decode_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        stego_text = file.read()
    
    if "\n" not in stego_text:
        print("No hidden message found.")
        return ""

    cover, encoded_str = stego_text.rsplit("\n", 1)
    tokens = encoded_str.split("\u200b")

    bits = ""
    for token in tokens:
        if token == " ":
            bits += '0'
        elif token == "  ":
            bits += '1'

    if len(bits) < 32:
        print("No valid message found.")
        return ""

    header = bits[:32]
    message_length = int(header, 2)

    total_bits = 32 + (message_length * 8)
    message_bits = bits[32:total_bits]

    message_bytes = bytearray()
    for i in range(0, len(message_bits), 8):
        byte_chunk = message_bits[i:i+8]
        if len(byte_chunk) < 8:
            break
        message_bytes.append(int(byte_chunk, 2))

    try:
        decoded_message = message_bytes.decode('utf-8', errors='replace')
    except Exception:
        decoded_message = ""

    print("Decoded message:", decoded_message)
    return decoded_message

# Example usage:
file_path = "textfile.txt"

# Hiding the message
secret_message = input("Enter the text to hide: ")
encode_text_in_file(file_path, secret_message)

# Retrieving the message
decode_text_from_file(file_path)
