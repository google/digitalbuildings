# GUID Generator

The GUID Generator allows you to generate GUIDs for Building Configuration
instances having missing or partially filled GUID fields.

The generator cannot be run as a standalone application and must be run with the
[toolkit](../toolkit.py).


# Install

To install please follow the instructions below.

## First create a virtual env

Create the virutal environment with `virtualenv` followed by the environment name, in this example: `tooling`

```
virtualenv tooling
```


Activate the virtual environment

Mac OS / Linux:
```
source tooling/bin/activate
```

Windows
```
tooling\Scripts\activate
```


Then you can either use pip or setuptools.

## Pip

To instantiate the generator and its dependencies:
1. Run `python3 -m pip install --upgrade pip` to ensure that your Python package management tools are up-to-date.
2. Run `python3 -m pip install .` from the following directories:
* digitalbuildings/tools/validators/ontology_validator
* digitalbuildings/tools/validators/instance_validator
* digitalbuildings/tools/guid_generator



## Setup (to be depcrecated)

To instantiate the generator and its dependencies, run
`sudo python setup.py install`



