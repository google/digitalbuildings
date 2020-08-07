import sys
import os
from PIL import Image

import ibr_pb2

from boundary_extraction.boundary_extraction import extract_boundary
from imagedata_creation.imagedata_creation import get_image_data
import utils

if __name__ == '__main__':

    # Read image filename
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], 'image file name')
        sys.exit(-1)

    # Initialize new IBR
    new_ibr = ibr_pb2.InternalBuildingRepresentation()
    vis = ibr_pb2.InternalBuildingRepresentation.Visualization()
    filename = sys.argv[1]

    # Store boundary data in IBR
    coords = extract_boundary(filename)
    utils.set_IBR_coordinates_lookup(new_ibr, utils.list_to_bytearray(coords, '>f4'))
    utils.set_IBR_boundary(new_ibr, utils.list_to_bytearray([0, len(coords)-3], '>i4'))

    # Get image data
    image_data_raw = get_image_data(filename)
    # Flip the original image for display
    image_obj = Image.open(filename)
    flipped_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_image_name = ''.join(filename.split('.')[:-1]) + '_flipped.' + filename.split('.')[-1]
    flipped_image.save(flipped_image_name)
    with open(flipped_image_name, 'rb') as image_file:
        image_bytes = image_file.read()
    os.remove(flipped_image_name)

    # Create Visualization Layer
    vis.id = 'temp'
    vis.encoding_type = 3
    utils.set_visualization_image_data(vis, image_data_raw, image_bytes)
    new_ibr.visualization.append(vis)

    # Write to output
    output_filename = ''.join(filename.split('.')[:-1])
    f = open(output_filename+'.ibr', 'wb')
    f.write(new_ibr.SerializeToString())
    f.close()
