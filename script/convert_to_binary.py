# Step 1: Reading the file in binary mode
with open('src/input/test_subject_001.mp4', 'rb') as file:
    binary_content = file.read()

# Step 2: Convert to binary string representation
binary_string = ''.join(format(byte, '08b') for byte in binary_content)

# Step 3: Save the binary string to a .txt file
with open('src/output/output_txt.txt', 'w') as output_file:
    output_file.write(binary_string)
