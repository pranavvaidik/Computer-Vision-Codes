from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

#figure()
cv2.imshow("Image", image)


cv2.imwrite("newimage.jpg", image)

corner = image[0:100,0:100]
cv2.imshow("corner",corner)

image[0:100,0:100] = (0,255,0)
#(b,g,r) = image[0,0]
#print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))
cv2.imshow("updated",image)
cv2.waitKey(0)

