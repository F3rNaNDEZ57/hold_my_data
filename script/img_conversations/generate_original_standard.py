from PIL import Image
import numpy as np
import zlib
import os

# Step 1: Load each image in the order they were saved
image_folder = 'src/output/test_subject_003'
image_files = sorted(os.listdir(image_folder), key=lambda x: int(x.split('_')[-1].split('.')[0]))

all_pixel_values = []

for image_file in image_files:
    with Image.open(os.path.join(image_folder, image_file)) as img:
        # Check image size
        width, height = img.size
        if width != 512 or height != 512:
            pixel_values = np.asarray(img)[:width, :height].flatten()
        else:
            pixel_values = np.asarray(img).flatten()

        all_pixel_values.append(pixel_values)

# Concatenate pixel values
all_pixel_values = np.concatenate(all_pixel_values)

# Convert the numpy array to bytes
compressed_data_bytes = all_pixel_values.tobytes()

# Step 3: Decompress the concatenated data
original_data = zlib.decompress(compressed_data_bytes)

# Step 4: Save the decompressed data as the original file
with open('src/output/reconstructed_test_subject_003.msi', 'wb') as file:
    file.write(original_data)
