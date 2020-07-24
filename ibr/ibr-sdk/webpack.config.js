const path = require('path');

module.exports = {
  entry: './src/index.js',

  output: {
  	library: 'IBRSDK',
    path: path.resolve(__dirname, 'dist'),
    filename: 'main.js'
  }
};