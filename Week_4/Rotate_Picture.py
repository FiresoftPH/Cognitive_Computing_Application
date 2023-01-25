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

(h, w) = img.shape[:2]
center=(w//2,h//2) 

M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
M = cv2.getRotationMatrix2D(center, -90, 1.0)

rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

cv2.waitKey(0)