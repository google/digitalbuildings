import test from 'ava';
import {Layer} from '../ibr-sdk/class/Layer.js';

test.before( (t) => {
  const coordsIndices1 = new Int8Array([0, 0, 0, 0, 0, 0, 8, 28]);
  t.context.jsonData1 = {
    coordinate_indices: coordsIndices1,
    data: 'coordinate_indices',
    encoding_type: 1,
    id: 'US-SVL-TC2-1',
    image_data: null,
  };

  t.context.layer = new Layer( t.context.jsonData1 );
});

test('should have an ID', t => {
  t.is(t.context.layer.getID(), t.context.jsonData1.id);
});

test('should convert coordinates indices to Int32 Array', t => {
  t.deepEqual(t.context.layer.getCoordinatesIndices(), new Uint32Array( [0, 2076] ));
});

test('should have data recorded', t => {
  t.deepEqual( t.context.layer.getData(), t.context.jsonData1.data );
});

test('should have encoding type recorded', t => {
  t.deepEqual(t.context.layer.getEncodingType(), t.context.jsonData1.encoding_type );
});

test('should have image data recorded', t => {
  t.deepEqual(t.context.layer.getImageData(), t.context.jsonData1.image_data );
});

