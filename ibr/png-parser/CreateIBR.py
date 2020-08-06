import ibr_pb2
import sys
from boundary_extraction.boundary_extraction import extract_boundary
from imagedata_creation.imagedata_creation import get_image_data
from utils import *

# Read image filename
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "image file name")
    sys.exit(-1)

# Initialize new IBR
new_ibr = ibr_pb2.InternalBuildingRepresentation()
vis = ibr_pb2.InternalBuildingRepresentation.Visualization()
filename = sys.argv[1]

# Store boundary data in IBR
coords = extract_boundary(filename)
set_IBR_coordinates_lookup(new_ibr, list_to_bytearray(coords, '>f4'))
set_IBR_boundary(new_ibr, list_to_bytearray([0, len(coords)-3], '>i4'))

# Get image data
image_data_raw = get_image_data(filename)

# Create Visualization Layer
vis.id = 'temp'
vis.encoding_type = 3
set_visualization_image_data(vis, image_data_raw)
new_ibr.visualization.append(vis)

# Write to output
f = open("new_ibr.ibr", "wb")
f.write(new_ibr.SerializeToString())
f.close()
