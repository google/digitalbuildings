# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Main module for DBO explorer."""
from lib import explorer
from lib import model

import pyfiglet

from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string('changed', None, 'Path to an alternate ontology')
flags.DEFINE_boolean('debug', False, 'Produces debugging output')

def main(argv):
  """Main method for DBO explorer."""
  if FLAGS.debug:
    print('non-flag arguments:', argv)
  figlet_out = pyfiglet.figlet_format('DBO Explorer', font='digital')
  print(figlet_out)
  print('Starting DBO explorer')
  my_ontology = explorer.Build(FLAGS.changed)
  done = False
  while not done:
    function_choice = input(
        '\nHow would you like to query DBO\n' +
        '1: Get fields for a type name\n' +
        '2: Get types for a list of fields\n' +
        '3: Validate a field name\n' +
        'q: quit\n' +
        'Please select an option: '
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

if __name__ == '__main__':
  app.run(main)
