load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = 'CreateIBR',
    main = 'CreateIBR.py',
    srcs = ['CreateIBR.py', utils],
    python_version = "PY3",
    deps = ['//boundary_extraction:boundary_extraction',
    '//imagedata_creation:imagedata_creation',
    'utils:*'],
)