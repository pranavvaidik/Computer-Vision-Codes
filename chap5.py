import numpy as np
import cv2

canvas = np.zeros((300,300,3),dtype="uint8")

for i in range(0,canvas.shape[0],20):
	for j in range(0,canvas.shape[1],20):
		cv2.rectangle(canvas,(i,j),(i+10,j+10),(0,0,255),-1)
		cv2.rectangle(canvas,(i+10,j+10),(i+20,j+20),(0,0,255),-1)

center = (canvas.shape[1]//2,canvas.shape[0]//2)
cv2.circle(canvas,center,50,(0,255,0),-1)

cv2.imshow("image",canvas)
cv2.waitKey(0)
