import numpy as np
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
yuv  = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)

(Y,U,V) = cv2.split(yuv)

cv2.imshow("original",gray-Y)

print gray-Y
cv2.imshow("Y",Y)

from skimage.segmentation import slic

segments = slic(image,n_segments=250,compactness=10,sigma=1)

#shifted = imutils.resize(image,width = 100)
segments = 255*segments

cv2.imshow("segments",segments)
cv2.waitKey(0)


