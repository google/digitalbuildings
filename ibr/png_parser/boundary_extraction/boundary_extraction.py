import numpy as np
import cv2

def extract_boundary(filename):

    # Read file input
    img = cv2.imread(filename) # type numpy.ndarray

    # Preprocessing
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (thresh, bw) = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    bw = cv2.bitwise_not(bw)
    kernel = np.ones((3, 3), np.uint8)
    bw = cv2.dilate(bw, kernel, iterations=1)
    bw = cv2.erode(bw, kernel, iterations=1)

    # extract contour from image
    contours, hierarchy = cv2.findContours(bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize return list of coordinates
    coords = []
    # Only extracting external contour, hence variable contours only has 1 element
    for points in contours[0]:
        for point in points:
            coords.append(point[0])
            coords.append(point[1])
            coords.append(0)
    return coords