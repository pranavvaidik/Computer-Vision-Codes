from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True,help ="Path to the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)

plt.figure()
plt.title("gray hist")
hist = cv2.calcHist(img,[0],None,[256],[0,256])
plt.plot(hist)


ch = cv2.split(image)
colors = ("b","g","r")

plt.figure()
plt.title("color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")


for (chan,color) in zip(ch,colors):
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist, color = color)
	plt.xlim([0,256])

fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([ch[1],ch[0]],[0,1],None,[8,8],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title("2d color hist GB")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([ch[2],ch[1]],[0,1],None,[8,8],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title("2d color hist RG")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([ch[0],ch[2]],[0,1],None,[8,8],[0,256,0,256])
p = ax.imshow(hist,interpolation = "nearest")
ax.set_title("2d color hist BR")
plt.colorbar(p)

print("2d hist shape : {}, with {} values".format(hist.shape,hist.flatten().shape[0]))


#plt.figure()
hist = cv2.calcHist([image], [0, 1, 2],None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(
hist.shape, hist.flatten().shape[0]))

plt.show()
#cv2.waitKey(0)

