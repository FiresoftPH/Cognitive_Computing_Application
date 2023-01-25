import cv2
import numpy as np

mask = np.zeros((300, 300, 3), dtype = "uint8")

radius = 150
for x in range(6):

    cv2.circle(mask, (150, 150), radius - (25*x), (255, 255, 255), 3)

cv2.imshow("mask",  mask)
cv2.waitKey(0)

source = cv2.imread("Week_4\Cat03.jpg")

print(source.shape)

# source = cv2.resize(source, (300, 300))

mask = np.zeros(source.shape[:2], dtype = "uint8")
# (cX, cY) = (source.shape[1] // 2, source.shape[0] // 2)

cv2.imshow("original", source)
cv2.waitKey(0)

source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
cv2.imshow("sadge", source)
cv2.waitKey(0)

radius = 150
for x in range(6):

    cv2.circle(mask, (639 // 2, 640 // 2), radius - (25*x), (255, 255, 255), 3)

cv2.waitKey(0)

masked = cv2.bitwise_and(source, source, mask = mask)

cv2.imshow("finished", masked)
cv2.waitKey(0)