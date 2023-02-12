import cv2
import numpy as np

image_norm = cv2.imread("Week_6\coin.png")
image_o = cv2.imread("Week_6\coin.png", 0)

image = cv2.GaussianBlur(image_o, (5, 5), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                                      

cv2.drawContours(image_norm, contours, -1, (255, 0, 0), 2)
                
cv2.imshow('coins', image_norm)
cv2.waitKey(0)

