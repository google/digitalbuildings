from pykwalify.core import Core

def validate_file(source, schema):
    c = Core(source_file=source, schema_files=[schema])
    res = c.validate(raise_exception=True)
    return res

res = None

res = validate_file('bad_type_id.yaml', 'schema.yaml')

print(res)

'''
- show how it works
- show it catching a bad example
- show my issues with it

- connections, translation, metadata loose checking
    - validation done later manually
    OR
    - can make custom validation rules to make it stricter

validator command-line input, find elegant way to handle all the stricter validation for 1 day w/ pykwalify, then switch to Antlr
'''
