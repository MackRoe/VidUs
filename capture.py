import cv2
import time

# create object. zero for camera
video = cv2.VideoCapture(0)

# create a frame object
check, frame = video.read()

print(check)
print(frame)  # represents image

# shut down the camera
video.release()
