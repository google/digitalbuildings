import cv2

def get_image_data(filename):

    # Read file input
    img = cv2.imread(filename)

    # Create output list (length, width)
    image_data = (img.shape[1], img.shape[0])

    return image_data
