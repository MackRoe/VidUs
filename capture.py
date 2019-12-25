import cv2
import time

# create object. zero for camera
video = cv2.VideoCapture(0)

# create a frame object
check, frame = video.read()

print(check)
print(frame)  # represents image

# show the frame
cv2.imshow("Capturing", frame)

# any key to escape
cv2.waitKey(0)

# shut down the camera
video.release()
