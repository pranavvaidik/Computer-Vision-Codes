import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50, 150, apertureSize = 3)

cv2.imshow("edges", edges)
cv2.imshow("gray", gray)

lines = cv2.HoughLinesP(edges,2,2*np.pi/180,200, minLineLength = 30, maxLineGap = 2)

print "number of lines = ", lines.shape[0]

for i in np.arange(lines.shape[0]):
#	print "line ",i," is ", lines[i]
	#print lines[1]
#	print "x1 is: ", lines[i,0,0]
#	print "x2 is: ", lines[i,0,1]
#	print "x3 is: ", lines[i,0,2]
#	print "x4 is: ", lines[i,0,3]

	x1 = lines[i,0,0]
	y1 = lines[i,0,1]
	x2 = lines[i,0,2]
	y2 = lines[i,0,3]

	cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("lines",image)
#print lines[0]
cv2.waitKey(0)
