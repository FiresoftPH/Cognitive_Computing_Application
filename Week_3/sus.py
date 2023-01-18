import cv2
import numpy as np

PATH = "Week_3\sunset_image.png"
PATH.replace("/", "\\")

img = cv2.imread(PATH)
height, width, channels = img.shape
b, g, r = cv2.split(img)

zeros = np.zeros((height, width,1), np.uint8)
b = cv2.merge((b,zeros,zeros))
g = cv2.merge((zeros,g,zeros))
r = cv2.merge((zeros,zeros,r))

img[0:int(height/2), int(width/2)::] = b[0:int(height/2), int(width/2)::]
img[int(height/2)::, 0:int(width/2)] = g[int(height/2)::, 0:int(width/2)]
img[int(height/2)::, int(width/2)::] = r[int(height/2)::, 0:int(width/2)]

cv2.imshow('image', img)
cv2.waitKey(0)