import cv2
import numpy as np
import glob
 
# list to store imgs
img_array = []
# fetch images with glob
for filename in glob.glob('C:/New folder/Images/*.jpg'):
    # read the imgs with cv2.imread()
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    # store the imgs in a list 
 
# create a VideoWriter object
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
    # save imgs to video file
out.release()
# release the video file and destroy all windows

# https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/
