import zlib

#Read the file
with open('src/output/binary.txt', 'rb') as f: # Open in binary read mode
    binary_string = f.read()

#Compress the data
compressed_data = zlib.compress(binary_string)

#Save the compressed data (optional)
with open('src/output/compressed_data.txt', 'wb') as f: # Open in binary write mode
    f.write(compressed_data)
