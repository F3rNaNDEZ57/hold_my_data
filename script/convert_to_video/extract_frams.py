import cv2
import os

video_path = 'src/output/nobody2021.avi'
output_folder = 'src/output/extracted_frames'

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the video
cap = cv2.VideoCapture(video_path)

frame_number = 0

while True:
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    frame_filename = os.path.join(output_folder, f'frame_{frame_number:04d}.png')
    cv2.imwrite(frame_filename, frame)
    frame_number += 1

cap.release()

print(f"Extracted {frame_number} frames to {output_folder}")
