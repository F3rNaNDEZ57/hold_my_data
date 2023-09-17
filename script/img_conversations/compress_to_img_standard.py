import zlib
from PIL import Image
import numpy as np
import os

input_path = 'src/input/test_subject_001.mp4'

# Read the file in binary mode
with open(input_path, 'rb') as file:
    binary_content = file.read()

# Compress the binary content
compressed_data = zlib.compress(binary_content)

# Convert compressed data to pixel values
pixel_values = np.frombuffer(compressed_data, dtype=np.uint8)

# Calculate padding
pixels_per_image = 512 * 512 * 3
padding_needed = pixels_per_image - (len(pixel_values) % pixels_per_image)

# Add padding
pad_values = np.zeros(padding_needed, dtype=np.uint8)
pixel_values_padded = np.concatenate([pixel_values, pad_values])

# Split into 512x512 chunks
chunks = np.split(pixel_values_padded, len(pixel_values_padded) / pixels_per_image)

file_name = os.path.basename(input_path)
output_folder_name = os.path.splitext(file_name)[0]

output_dir = os.path.join('src/output', output_folder_name)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save each chunk
for idx, chunk in enumerate(chunks):
    img_array = np.reshape(chunk, (512, 512, 3))
    img = Image.fromarray(img_array, 'RGB')
    img.save(os.path.join(output_dir, f'compressed_image_{idx}.png'))
