import commonjs from 'rollup-plugin-commonjs'
import replace from '@rollup/plugin-replace';
import * as propTypes from 'prop-types';

const NODE_ENV = process.env.NODE_ENV || "development";

export default [
  {
    input: 'src/index.js',
    output: [
      {
        format: 'umd',
        name: 'IBRSDK',
        file: 'dist/main.js',
        indent: '\t',
        globals: {
          'three': 'THREE',
        },
      },
    ],
    plugins: [
        replace({
          "process.env.NODE_ENV": JSON.stringify(NODE_ENV)
        }),
        commonjs({
          namedExports: {
            'prop-types': Object.keys(propTypes),
          },
        })
    ],
    external: [
      'three', 'pbf'
    ],
  },
];
