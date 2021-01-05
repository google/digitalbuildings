import test from 'ava';
import {Visualization} from '../src/Visualization.js';

test.before( (t) => {
  const coordsIndices1 = new Uint8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  t.context.jsonData1 = {
    coordinate_indices: coordsIndices1,
    data: 'coordinate_indices',
    encoding_type: 1,
    id: 'US-SVL-TC2-1',
    image_data: undefined,
  };
  const coordsLookup = Float32Array.from(
     [269.67669677734375, 165.02369689941406, 0, 295.67669677734375,
      165.02369689941406] );
  t.context.visualization = new Visualization( t.context.jsonData1, coordsLookup );
});

test('should have an ID', t => {
  t.is(t.context.visualization.getID(), t.context.jsonData1.id);
});

test('should convert coordinates indices to Int32 Array', t => {
  t.deepEqual(t.context.visualization.getCoordinatesIndices(), new Uint32Array( [0, 2076] ));
});

test('should have data recorded', t => {
  t.deepEqual( t.context.visualization.getData(), t.context.jsonData1.data );
});

test('should have encoding type recorded', t => {
  t.deepEqual(t.context.visualization.getEncodingType(), t.context.jsonData1.encoding_type );
});

test('should have image data recorded', t => {
  t.deepEqual(t.context.visualization.getImageData(), t.context.jsonData1.image_data );
});

test('should be converted back to JSON format', (t) => {
  t.deepEqual(t.context.visualization.toJson(),
      t.context.jsonData1 );
});
