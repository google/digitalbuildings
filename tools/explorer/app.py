"""Main module for DBO explorer."""
from lib import explorer
from lib import model

import pyfiglet

from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string('alt', None, 'Path to an alternate ontology')
flags.DEFINE_boolean('debug', False, 'Produces debugging output')

def main(argv):
  """Main method for dbo.tools.explorer which runs explorer as an abseil app"""
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  figlet_out = pyfiglet.figlet_format('DBO Explorer', font='digital')
  print(figlet_out)
  print('Starting DBO explorer')
  my_ontology = explorer.Build(FLAGS.alt)
  done = False
  while not done:
    function_choice = input(
        '\nWhat would you like to do?\n' +
        '1: Get fields for a type name\n' +
        '2: Get types for a list of fields\n' +
        '3: Validate a field name\n' +
        'q: quit\n' +
        'your choice: '
    )
    if function_choice == '1':
      namespace = input('Enter a namespace: ').upper()
      type_name = input(f'Enter a type name defined in {namespace}: ').upper()
      fields = my_ontology.GetFieldsForTypeName(namespace, type_name)
      for field in fields:
        print(field)
    elif function_choice == '2':
      print('This functionality is still under construction.\n'+
            'Please pick another option.')
    elif function_choice == '3':
      namespace = input('Enter a namespace: ').upper()
      field_name = input('Enter a field name to validate: ')
      standard_field = model.StandardField(namespace, field_name)
      field_is_valid = my_ontology.IsFieldValid(standard_field)
      if namespace == '':
        namespace = 'global'
      print(f'{field_name} is defined in {namespace}: {field_is_valid}')
    elif function_choice == 'q':
      print('bye bye')
      done = True
    else:
      print(
          'You entered: ' + function_choice + '\n' +
          'Please enter a valid input'
      )

if __name__ == "__main__":
  app.run(main)
