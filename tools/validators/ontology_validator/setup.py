from setuptools import setup, find_packages
# with open("README.md", "r") as fh:
#   long_description = fh.read()
setup(
    name='ontology-yaml-validator',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='',
    author_email='',
    description='',
    packages=find_packages(),
    install_requires=['absl-py', 'pyglib', 'pyyaml', 'absl-py'],
    python_requires='>=3.6',
)
