import test from 'ava';
import { IBRObject } from '../src/IBRObject.js';
import {BlockingGrid} from '../src/BlockingGrid.js';
import { Visualization } from '../src/Visualization.js';

test.before( (t) => {
  const coordsLookup = new Uint8Array([67, 134, 214, 158, 67, 37, 6, 17,
    0, 0, 0, 0, 67, 147, 214, 158, 67, 37, 6, 17]);
  const blockingCoordsIndices = new Uint8Array([0, 0, 8, 31, 0, 0, 8, 34]);
  const coordsIndices1 = new Uint8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  const coordsIndices2 = new Uint8Array([0, 0, 8, 31, 0, 0, 8,
    34, 0, 0, 8, 37, 0, 0, 8, 40]);
  t.context.jsonData1 = {
    blocking_grid: null,
    boundary: undefined,
    guid: null,
    name: undefined,
    connections: [],
    coordinates_lookup: null,
    external_reference: [],
    metadata: null,
    structural_type: undefined,
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
            image_data: undefined,
          },
        },
        boundary: undefined,
        guid: 'US-SVL-TC2-1',
        name: 'US-SVL-TC2-1',
        connections: [],
        coordinates_lookup: coordsLookup,
        external_reference: [],
        metadata: null,
        structural_type: undefined,
        structures: [],
        visualization:
        [
          {
            coordinate_indices: coordsIndices1,
            data: 'coordinate_indices',
            encoding_type: 1,
            id: 'test1',
            image_data: undefined,
          },
          {
            coordinate_indices: coordsIndices2,
            data: 'coordinate_indices',
            encoding_type: 1,
            id: 'test2',
            image_data: undefined,
          },
        ],
      },
    ],
  };

  t.context.ibrObject1 = new IBRObject( t.context.jsonData1 );
  t.context.ibrObject2 = new IBRObject( t.context.jsonData1.structures[0] );
});

test('IBRObject default name', (t) => {
  t.is( t.context.ibrObject1.getName(), undefined );
});

test('IBRObject call getVisualizations() when no visualizations', (t) => {
  t.deepEqual( t.context.ibrObject1.getVisualizations(), new Map() );
});

test('IBRObject does not have visualizations', (t) => {
  t.false( t.context.ibrObject1.hasVisualizations );
});

test('IBRObject has visualizations size', (t) => {
  t.is( t.context.ibrObject2.getVisualizations().size, 2 );
});

test('IBRObject has visualizations', (t) => {
  t.true(t.context.ibrObject2.hasVisualizations);
});

test('IBRObject does not have coordinate lookup', (t) => {
  t.false(t.context.ibrObject1.hasCoordinatesLookup);
  t.is(t.context.ibrObject1.getCoordinates(), undefined);
});

test('IBRObject has coordinate lookup', (t) => {
  t.true(t.context.ibrObject2.hasCoordinatesLookup);
  t.deepEqual(t.context.ibrObject2.getCoordinates(), Float32Array.from(
      [269.67669677734375, 165.02369689941406, 0, 295.67669677734375,
        165.02369689941406] ));
});

test('record sub structures', (t) => {
  t.is( t.context.ibrObject1.getSubStructures(),
      t.context.jsonData1.structures );
});

test('has blocking grid', (t) => {
  t.deepEqual( t.context.ibrObject2.getBlockingGrid(),
      new BlockingGrid(t.context.jsonData1.structures[0].blocking_grid,
      t.context.ibrObject2.getCoordinates()));
});

test('should be converted back to JSON format', (t) => {
  t.deepEqual(t.context.ibrObject1.toJson(),
      t.context.jsonData1 );
  t.deepEqual(t.context.ibrObject2.toJson(),
        t.context.jsonData1.structures[0] );
});
