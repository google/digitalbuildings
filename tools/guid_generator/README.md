# GUID Generator

The GUID Generator allows you to generate GUIDs for Building Configuration
instances having missing or partially filled GUID fields.

The generator cannot be run as a standalone application and must be run with the
[toolkit](../toolkit.py).


# Install

To install the guid generator please follow one of the two.

## Pip

To instantiate the generator and its dependencies:
1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install -r requirements.txt ` from the following directories, in order:
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/guid_generator


## Setup

To instantiate the generator and its dependencies, run
`sudo python setup.py install`



