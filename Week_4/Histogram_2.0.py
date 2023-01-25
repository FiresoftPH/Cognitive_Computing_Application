import cv2

def run_histogram_equalization(image_path):
    img = cv2.imread(image_path)

    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)

    cv2.imshow('equalized_img', equalized_img)
    cv2.waitKey(0)

    cv2.imshow("Original_Image", img)
    cv2.waitKey(0)

run_histogram_equalization("Week_3\sunset_image.png")