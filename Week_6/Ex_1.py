import numpy as np
import cv2

img = cv2.imread("Week_6\\coin.png", cv2.IMREAD_GRAYSCALE)

width = img.shape[1]
height = img.shape[0]

def thresholding(max):
    for item in range(height):
        for item2 in range(width):
            if img[item][item2] > max:
                img[item][item2] = 255

            else:
                img[item][item2] = 0

thresholding(127)
cv2.imshow("Image", img)
cv2.waitKey(0)

"""
Explanation for the picture 1 and 2. The left picture is THRESH_TOZERO because the brightest part is still bright and the darkest part
is dark. Unlike the right picture.
"""

