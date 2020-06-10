from pykwalify.core import Core

c = Core(source_file='test_data.yaml', schema_files=['schema.yaml'])
res = c.validate(raise_exception=True)
print(res)