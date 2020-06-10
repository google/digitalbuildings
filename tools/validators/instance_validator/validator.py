from pykwalify.core import Core

def validate_file(source, schema):
    c = Core(source_file=source, schema_files=[schema])
    res = c.validate(raise_exception=True)
    return res

# bad_1.yaml and bad_2.yaml are not immediately caught because of type: any
# we can invalidate them later because their parsed outputs have None
validate_file('bad_1.yaml', 'schema.yaml')
validate_file('bad_2.yaml', 'schema.yaml')

# bad_3 is caught because type and id require type: str
validate_file('bad_3.yaml', 'schema.yaml')

validate_file('bad_4.yaml', 'schema.yaml')
