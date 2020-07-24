
export default [
    {
        input: 'src/index.js',
        output: [
            {
                format: 'umd',
                name: 'IBRSDK',
                file: 'dist/main.js',
                indent: '\t'
            }
        ]
    },
];