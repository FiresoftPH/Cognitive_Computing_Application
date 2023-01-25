import numpy as np
import cv2 

img = cv2.imread('Week_3\cat_image.png',0)
rows,cols = img.shape
M = np.float32([[1,0,25],[0,1,50]]) # right & down 
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Shifted Down and Right',dst)


M = np.float32([[1,0,-50],[0,1,-90]]) # left & up 
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('Shifted Up and Left',dst)

cv2.waitKey(0)