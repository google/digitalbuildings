import test from 'ava';
import { IBRObject } from '../ibr-sdk/class/IBRObject.js';
import { Layer } from '../ibr-sdk/class/Layer.js';

test.before( t => {
  t.context.defaultName = 'ibrData.name';
  const coordsLookup = new Int8Array([67, 134, 214, 158, 67, 37, 6, 17, 0, 0, 0, 0,
      67, 147, 214, 158, 67, 37, 6, 17]);
  const blockingCoordsIndices = new Int8Array([0, 0, 8, 31, 0, 0, 8, 34]);
  const coordsIndices1 = new Int8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  const coordsIndices2 = new Int8Array([0, 0, 8, 31, 0, 0, 8,
      34, 0, 0, 8, 37, 0, 0, 8, 40]);
  t.context.jsonData1 = {
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

  t.context.ibrObject1 = new IBRObject( t.context.jsonData1 );
  t.context.ibrObject2 = new IBRObject( t.context.jsonData1.structures[0] );

});

test('IBRObject default name', t => {
  t.is( t.context.ibrObject1.getName(), t.context.defaultName );
});

test('IBRObject call getLayers() when no layers', t => {
  t.deepEqual( t.context.ibrObject1.getLayers(), new Map() );
});

test('IBRObject does not have layers', t => {
  t.false( t.context.ibrObject1.hasLayers );
});

test('IBRObject has layers size', t => {
  t.is( t.context.ibrObject2.getLayers().size, 2 );
});

test('IBRObject has layers', t => {
  t.true(t.context.ibrObject2.hasLayers);
});

test('IBRObject does not have coordinate lookup', t => {
  t.false(t.context.ibrObject1.hasCoordinatesLookup);
  t.is(t.context.ibrObject1.getCoordinates(), undefined);
});

test('IBRObject has coordinate lookup', t => {
  t.true(t.context.ibrObject2.hasCoordinatesLookup);
  t.deepEqual(t.context.ibrObject2.getCoordinates(), [269.67669677734375, 165.02369689941406, 0, 295.67669677734375, 165.02369689941406]);
});

test('record sub structures', t => {
  t.is( t.context.ibrObject1.getSubStructures(), t.context.jsonData1.structures );
});
