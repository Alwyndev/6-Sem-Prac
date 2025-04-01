def compute_checksum(hex_values):
    # Convert hex string to bytes
    data = bytearray(bytes.fromhex(hex_values.replace(" ", "").replace("\n", "")))

    # Ensure we only take the first 20 bytes (IPv4 header length without options)
    ip_header = data[:20]
    
    # Set checksum field to zero (bytes 10 and 11 in the header)
    ip_header[10] = 0
    ip_header[11] = 0

    # Compute one's complement sum
    checksum = 0
    for i in range(0, len(ip_header), 2):
        word = (ip_header[i] << 8) + ip_header[i + 1]
        checksum += word

        # Handle carry bits by wrapping around
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    # Final one's complement
    checksum = ~checksum & 0xFFFF
    return f"{checksum:04X}"


# Extracting only the IPv4 Header (first 20 bytes from the provided hex)
hex_values = """
45 00
00 28 c4 ab 40 00 80 06 00 00 c0 a8 15 4d 14 c0
2c 44 cf 35 01 bb 8b 07 e6 b8 9e 93 cb 2a 50 10
00 fa 17 14 00 00
"""

# Compute the checksum
computed_checksum = compute_checksum(hex_values)
print(f"Computed Checksum: 0x{computed_checksum}")
