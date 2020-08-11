import babel from '@rollup/plugin-babel';
import {nodeResolve} from '@rollup/plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs'
import replace from '@rollup/plugin-replace';
import * as react from 'react';
import * as reactDom from 'react-dom';
import * as reactIs from 'react-is';
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
        nodeResolve(),
        babel({
          exclude: 'node_modules/**',
          presets: ['@babel/env', '@babel/preset-react'],
          plugins: ['react-html-attrs']
        }),
        commonjs({
          namedExports: {
            react: Object.keys(react),
            'react-dom': Object.keys(reactDom),
            'react-is': Object.keys(reactIs),
            'prop-types': Object.keys(propTypes),
          },
        })
    ],
    external: [
      'three', 'pbf'
    ],
  },
];
