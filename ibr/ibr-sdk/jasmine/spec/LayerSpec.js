describe('Layer', function() {
  const defaultName = 'ibrData.name';
  const coordsIndices1 = new Int8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  const jsonData1 = {
    coordinate_indices: coordsIndices1,
    data: 'coordinate_indices',
    encoding_type: 1,
    id: 'US-SVL-TC2-1',
    image_data: null,
  };

  let layer;

  beforeAll(function() {
    layer = new Layer( jsonData1 );
  });

  it('should have an ID', function() {
    expect(layer.getID()).toEqual(jsonData1.id);
  });

  it('should convert coordinates indices to Int32 Array', function() {
    expect(layer.getCoordinatesIndices()).toEqual(new Uint32Array( [0, 2076] ));
  });

  it('should have data recorded', function() {
    expect(layer.getData()).toEqual( jsonData1.data );
  });

  it('should have encoding type recorded', function() {
    expect(layer.getEncodingType()).toEqual( jsonData1.encoding_type );
  });

  it('should have image data recorded', function() {
    expect(layer.getImageData()).toEqual( jsonData1.image_data );
  });

});
