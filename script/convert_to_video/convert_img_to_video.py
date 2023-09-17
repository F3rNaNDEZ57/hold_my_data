import cv2
import os

image_folder = 'src/output/Nobody.2021.1080p.AMZN.WEB-DL.x265.HEVCBay.com'
video_name = 'src/output/nobody2021.avi'

images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")], key=lambda x: int(x.split('_')[-1].split('.')[0]))

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'FFV1'), 30, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()
