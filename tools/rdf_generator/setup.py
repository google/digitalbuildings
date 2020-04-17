from setuptools import setup, find_packages
# with open("README.md", "r") as fh:
#   long_description = fh.read()
setup(
    name='ontology-rdf-generator',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='charbelk',
    author_email='charbelk@google.com',
    description='',
    packages=find_packages(),
    install_requires=['absl-py', 'pyglib', 'ruamel.yaml', 'absl-py', 'rdflib'],
    python_requires='>=3.6',
)
