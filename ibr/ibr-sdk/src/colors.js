// List of colors from jquery.color.js plugin
const Colors = {};

Colors.names =
[
  // Google Blue
  '#174ea6',
  '#185abc',
  '#1967d2',
  '#1a73e8',
  '#4285f4',
  // Google Red
  '#a50e0e',
  '#b31412',
  '#c5221f',
  '#d93025',
  '#ea4335',
  // Google Yellow
  '#e37400',
  '#ea8600',
  '#f29900',
  '#f9ab00',
  '#fbbc04',
  // Google Green
  '#0d652d',
  '#137333',
  '#188038',
  '#1e8e3e',
  '#34a853',
];

Colors.random = function() {
  const result = this.names[Math.floor(Math.random() *
  (this.names.length - 1))];
  return result;
};

export {Colors};
