import zlib
from PIL import Image
import numpy as np
import os

# File path
input_path = 'src/input/test_subject_001.mp4'

# Step 1: Read the file in binary mode
with open(input_path, 'rb') as file:
    binary_content = file.read()

# Step 2: Compress the binary content
compressed_data = zlib.compress(binary_content)

# Step 3: Convert compressed data to pixel values
pixel_values = np.frombuffer(compressed_data, dtype=np.uint8)

# Calculate how much padding is needed for the last image
pixels_per_image = 100 * 100 * 3
padding_needed = pixels_per_image - (len(pixel_values) % pixels_per_image)

# Add padding to the pixel values
pad_values = np.zeros(padding_needed, dtype=np.uint8)
pixel_values_padded = np.concatenate([pixel_values, pad_values])

# Split the reshaped data into chunks of 512x512x3
chunks = np.split(pixel_values_padded, len(pixel_values_padded) / pixels_per_image)

# Get the filename without extension and use it as the output folder name
file_name = os.path.basename(input_path)
output_folder_name = os.path.splitext(file_name)[0]

output_dir = os.path.join('src/output', output_folder_name)

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 4: Save each chunk as a 512x512 image
for idx, chunk in enumerate(chunks):
    img_array = np.reshape(chunk, (100, 100, 3))
    img = Image.fromarray(img_array, 'RGB')
    img.save(os.path.join(output_dir, f'compressed_image_{idx}.png'))
