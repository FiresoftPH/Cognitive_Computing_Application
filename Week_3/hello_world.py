import cv2

image = cv2.imread("husky.png")

(b, g, r) =  image[0.0]
print("Pixel at (0,0) Red: {} Green: {}, Blue P {}".format(r, g, b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("image", image)

cv2.waitkey(0)