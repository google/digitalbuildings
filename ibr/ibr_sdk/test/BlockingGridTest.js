import test from 'ava';
import {BlockingGrid} from '../src/BlockingGrid.js';
import {Visualization} from '../src/Visualization.js';

test.before( (t) => {
  const coordsIndices1 = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 2]);
  t.context.visualizationJson = {
    coordinate_indices: coordsIndices1,
    data: 'coordinate_indices',
    encoding_type: 1,
    id: 'US-SVL-TC2-1',
    image_data: undefined
  };
  t.context.coordsLookup = Float32Array.from(
     [269.67669677734375, 165.02369689941406, 0, 295.67669677734375,
      165.02369689941406] );
  t.context.blockingGridJson = {
    id: 'blocking_id',
    visualization: t.context.visualizationJson
  };
  t.context.blockingGrid = new BlockingGrid( t.context.blockingGridJson, t.context.coordsLookup );
});

test('should have an ID', t => {
  t.is(t.context.blockingGrid.getID(), t.context.blockingGridJson.id);
});

test('should have a Visualization', t => {
  t.deepEqual(t.context.blockingGrid.getVisualization(),
  new Visualization( t.context.visualizationJson, t.context.coordsLookup ));
});

test('should be converted back to JSON format', (t) => {
  t.deepEqual(t.context.blockingGrid.toJson(),
      t.context.blockingGridJson );
});
