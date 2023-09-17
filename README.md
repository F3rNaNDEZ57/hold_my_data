Using YouTube as a Storage Service: A Creative Approach
In this method, we convert any given file into a sequence of 512x512 images, then encode these images into a video and theoretically store it on platforms like YouTube. Retrieving the file involves downloading the video, extracting the frames, and decoding the content to get back the original file.

Step 1: Convert original file into 512x512 images
Read the file in binary mode.
Compress the file's binary data using zlib to reduce its size.
Convert the compressed data into pixel values suitable for image creation.
For the last image, padding might be required to fit the 512x512 size.
Save each chunk of pixel data as separate images.
[[script/compress_to_img.py]]

Step 2: Convert images to 30FPS video
Read all the images from the directory, making sure they're in the correct order.
Using OpenCV, create a video out of these images with 30FPS.
We need to use a lossless codec (like FFV1) to ensure no data loss during this encoding.
View code for Step 2

Step 3: Extract frames from the video
Using OpenCV, read the video file frame by frame.
Save each frame as an image.
View code for Step 3

Step 4: Convert images back to the original file
Read all the images and convert them to a byte array.
Concatenate all the byte data.
Remove any padding that was added in the first step.
Decompress the byte data using zlib.
Save the decompressed data to get back the original file.
View code for Step 4

Note: While this method might seem intriguing, it's important to understand that platforms like YouTube will re-encode uploaded videos. Therefore, even with lossless video compression on our side, YouTube's encoding can alter the data. It's crucial to test this approach thoroughly before relying on it for actual storage.
