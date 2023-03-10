import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Week_3\sunset_image.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
hist = cv2.calcHist([image], [0], None, [255], [0, 255])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)