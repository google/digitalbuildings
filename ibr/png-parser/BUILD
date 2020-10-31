load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = 'create_ibr',
    main = 'create_ibr.py',
    srcs = ['create_ibr.py', 'utils.py'],
    python_version = "PY3",
    deps = [
        '//boundary_extraction:boundary_extraction',
        '//imagedata_creation:imagedata_creation',
    ],
)