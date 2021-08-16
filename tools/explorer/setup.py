"""setup module for ontology explorer"""
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
@@ -13,16 +12,18 @@
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
# with open("README.md", "r") as fh:
#   long_description = fh.read()
setup(
    name='ontology-explorer',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='Travis Welch',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
)
