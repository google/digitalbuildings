describe('IBRObject', function() {
  const defaultName = 'ibrData.name';
  const coordsLookup = new Int8Array([67, 134, 214, 158, 67, 37, 6, 17, 0, 0, 0, 0,
      67, 147, 214, 158, 67, 37, 6, 17]);
  const blockingCoordsIndices = new Int8Array([0, 0, 8, 31, 0, 0, 8, 34]);
  const coordsIndices1 = new Int8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  const coordsIndices2 = new Int8Array([0, 0, 8, 31, 0, 0, 8,
      34, 0, 0, 8, 37, 0, 0, 8, 40]);
  const jsonData1 = {
    blocking_grid: null,
    boundary: null,
    guid: null,
    name: null,
    connections: [],
    coordinates_lookup: null,
    external_reference: [],
    metadata: null,
    structuralType: 0,
    visualization: [],
    structures:
    [
      {
        blocking_grid: {
          id: 'US-SVL-TC2-1-blocking-grid',
          visualization: {
            coordinate_indices: blockingCoordsIndices,
            data: 'coordinate_indices',
            encoding_type: 1,
            id: 'US-SVL-TC2-1-blocking-grid',
            image_data: null,
          },
        },
        boundary: null,
        guid: 'US-SVL-TC2-1',
        name: 'US-SVL-TC2-1',
        connections: [],
        coordinates_lookup: coordsLookup,
        external_reference: [],
        metadata: null,
        structuralType: 0,
        structures: [],
        visualization:
        [
          {
            coordinate_indices: coordsIndices1,
            data: 'coordinate_indices',
            encoding_type: 1,
            id: 'test1',
            image_data: null,
          },
          {
            coordinate_indices: coordsIndices2,
            data: 'coordinate_indices',
            encoding_type: 1,
            id: 'test2',
            image_data: null,
          },
        ],
      },
    ],
  };

  let ibrObject1;
  let ibrObject2;

  beforeAll(function() {
    ibrObject1 = new IBRObject( jsonData1 );
    ibrObject2 = new IBRObject( jsonData1.structures[0] );
  });

  describe('when IBRObject does not have a name', function() {
    it('should use the default name', function() {
      expect(ibrObject1.getName()).toEqual(defaultName);
    });
  });

  describe('when IBRObject does not have visualization layers', function() {
    it('should return a new Map Object when layers are requested', function() {
      expect(ibrObject1.getLayers()).toEqual(new Map());
    });

    it('should indicate IBR does not have layers', function() {
      expect(ibrObject1.hasLayers).toEqual(false);
    });
  });

  describe('when IBRObject has visualization layers', function() {

    it('should return a list of Layer Objects created from JSON visualization layer', function() {
      expect(ibrObject2.getLayers().size).toEqual(2);
      expect(ibrObject2.getLayers().get(ibrObject2.getLayerNames()[0])).toBeInstanceOf( Layer );
    });

    it('should indicate IBR has layers', function() {
      expect(ibrObject2.hasLayers).toEqual(true);
    });

  });

  describe('when IBRObject does not have coordinate lookup', function() {

    it('should indicate whether IBR has coordinate lookup', function() {
      expect(ibrObject1.hasCoordinatesLookup).toEqual(false);
      expect(ibrObject1.getCoordinates()).toEqual(undefined);
    });

  });

  describe('when IBRObject has coordinate lookup', function() {

    it('should indicate whether IBR has coordinate lookup', function() {
      expect(ibrObject2.hasCoordinatesLookup).toEqual(true);
      expect(ibrObject2.getCoordinates()).toEqual([269.67669677734375, 165.02369689941406, 0, 295.67669677734375, 165.02369689941406]);
    });

  });

  it('should have sub structures recorded', function() {
    expect(ibrObject1.getSubStructures()).toEqual( jsonData1.structures );
  });

});
