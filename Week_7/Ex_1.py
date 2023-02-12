import numpy as np
import cv2

def sobel_filter(img):

    array_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    array_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    padded_image = np.pad(img, ((1, 1), (1, 1)), 'constant')
    
    height, width = padded_image.shape
    
    gradient = np.zeros_like(img)
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Apply the x and y Sobel kernels to the current pixel
            gradient_x = (array_x * padded_image[y-1:y+2, x-1:x+2]).sum()
            gradient_y = (array_y * padded_image[y-1:y+2, x-1:x+2]).sum()
            
            # Compute the gradient magnitude
            gradient[y-1, x-1] = np.sqrt(gradient_x**2 + gradient_y**2)
    
    return gradient

img = cv2.imread("Week_6\coin.png", cv2.IMREAD_GRAYSCALE)

# Apply the Sobel filter
gradient = sobel_filter(img)
cv2.imshow('image', gradient)
cv2.waitKey()
cv2.destroyAllWindows()