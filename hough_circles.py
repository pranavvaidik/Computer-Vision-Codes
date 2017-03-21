import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50, 100, apertureSize = 3)

cv2.imshow("edges", edges)
cv2.imshow("gray", gray)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT ,dp = 2, minDist = 10, minRadius = 1)

if circles == None:
	print "no circles found"

else:
	print "number of circles = ", circles.shape[1]
	print circles
	for i in np.arange(circles.shape[1]):
		print circles[0,i]

		x1 = circles[0,i,0]
		y1 = circles[0,i,1]
		r1 = circles[0,i,2]
	
		cv2.circle(image,(x1,y1),r1,(0,0,255),2)

cv2.imshow("circles",image)
cv2.waitKey(0)
