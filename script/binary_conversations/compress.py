import zlib

# Step 1: Read the file in binary mode
with open('src/input/test_subject_001.mp4', 'rb') as file:
    binary_content = file.read()

# Step 2: Compress the binary content
compressed_data = zlib.compress(binary_content)

# Step 3: Save the compressed data to a file
with open('src/output/compressed_data.dat', 'wb') as output_file:
    output_file.write(compressed_data)
