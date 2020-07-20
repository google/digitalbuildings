const webpack = require('webpack');
const path = require('path');

module.exports = {
    entry: {
        entry: __dirname + '/ibr-sdk/build/ibr-sdk.js'
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    mode: 'production'
}