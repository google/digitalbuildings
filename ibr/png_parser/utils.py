import numpy as np

def set_IBR_guid(structure, guid):
    structure.guid = guid

def set_IBR_name(structure, name):
    structure.name = name

def set_IBR_structural_type(structure, structural_type):
    structure.structural_type = structural_type

def set_IBR_metadata(structure, metadata):
    structure.metadata = metadata

def set_IBR_coordinates_lookup(structure, coordinates_lookup):
    structure.coordinates_lookup = coordinates_lookup

def set_IBR_visualization(structure, visualization):
    structure.visualization = visualization

def set_IBR_boundary(structure, boundary):
    structure.boundary = boundary

def add_IBR_structure(structure, sub_structure):
    structure.structures.append(sub_structure)

def add_IBR_external_reference(structure, external_reference):
    structure.external_reference.append(external_reference)

def set_IBR_blocking_grid(structure, blocking_grid):
    structure.blocking_grid = blocking_grid

def add_IBR_connection(structure, connection):
    structure.connections.append(connection)

def set_visualization_image_data(visualization, image_data_raw, encoded_image):
    visualization.image_data.length = image_data_raw[0]
    visualization.image_data.width = image_data_raw[1]
    visualization.image_data.image = encoded_image

def list_to_bytearray(lst, dtype):
    return np.array(lst, dtype=dtype).tobytes()