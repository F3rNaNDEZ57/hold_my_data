def binary_string_to_bytes(binary_string):
    """Convert a binary string to bytes."""
    byte_arr = []
    
    # Split the string into chunks of 8 (since one byte is 8 bits)
    for i in range(0, len(binary_string), 8):
        byte_chunk = binary_string[i:i+8]
        byte_arr.append(int(byte_chunk, 2))
    
    return bytes(byte_arr)

# Step 1: Read the binary string from the .txt file
with open('src/output/output_txt.txt', 'r') as input_file:
    binary_string = input_file.read()

# Step 2: Convert the binary string back to bytes
byte_data = binary_string_to_bytes(binary_string)

# Step 3: Write the bytes to an .mp4 file
with open('src/output/reconstructed.mp4', 'wb') as output_file:
    output_file.write(byte_data)
