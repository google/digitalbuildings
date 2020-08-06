import cv2

def get_image_data(filename):

    # Read file input
    img = cv2.imread(filename)
    print(img.dtype)
    print(len(img))
    print(len(img[0]))
    print(img.shape[1])
    print(img.shape[0])

    # Convert np.ndarray to bytes
    buffer = img.tobytes()

    # Create output list (length, width)
    image_data = (img.shape[1], img.shape[0], buffer)

    return image_data
