import cv2
import time

# create object. zero for camera
video = cv2.VideoCapture(0)

# shut down the camera
video.release()
