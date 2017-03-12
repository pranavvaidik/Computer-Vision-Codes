from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True,help ="Path to the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

blurred = np.hstack([cv2.GaussianBlur(image, (3,3),0), cv2.GaussianBlur(image, (5,5),0), cv2.GaussianBlur(image, (7,7),0)])
cv2.imshow("blur", blurred)
cv2.waitKey(0)
