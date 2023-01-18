import cv2

PATH = "Week_3\sunset_image.png"
PATH.replace("/", "\\")

image = cv2.imread(PATH)
overlay = image.copy()

# Rectangle parameters
x, y, w, h = 386, 0, 386, 290

x1, y1, w1, h1 = 0, 290, 386, 290

x2, y2, w2, h2 = 386, 290, 386, 290

alpha = 0.7
  
# A filled rectangle
cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 0, 0), -1)
cv2.rectangle(overlay, (x1, y1), (x1 + w1, y1 + h1), (0, 120, 0), -1)
cv2.rectangle(overlay, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 100), -1)
  
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

cv2.imshow("filter", image_new)

cv2.waitKey(0)
  
cv2.destroyAllWindows()
