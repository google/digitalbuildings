# Copyright 2020 Google LLC
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
"""Placeholder for constants."""
import rdflib

DB = 'http://www.google.com/digitalbuildings/'
ONT_VERSION = '0.0.1'
BASE = DB + ONT_VERSION
DIGITAL_BUILDINGS_NS = rdflib.Namespace(BASE + '#')
STATES_NS = rdflib.Namespace(BASE + '/states#')
UNITS_NS = rdflib.Namespace(BASE + '/units#')
FACILITIES_NS = rdflib.Namespace(BASE + '/facilities#')
SUBFIELDS_NS = rdflib.Namespace(BASE + '/subfields#')
FIELDS_NS = rdflib.Namespace(BASE + '/fields#')
HVAC_NS = rdflib.Namespace(BASE + '/hvac#')

SUBFOLDER_NAMES = frozenset(
    {'subfields', 'states', 'fields', 'entity_types', 'units'})


# Ontology Metadata information
DCTERMS = rdflib.Namespace('http://purl.org/dc/terms#')
AUTHORS = ('Keith Berkoben, Trevor Sodorff')
CONTRIBUTORS = ('Charbel El Kaed')
ONT_DESCRIPTION = ('The Digital Buildings ontology is an open-source, '
                   'Apache-licensed development effort to create a uniform '
                   'schema for representing metadata in Google\'s buildings '
                   'real estate portfolio. It is inspired from Project Haystack'
                   ' and BrickSchema.')

GITHUB = 'https://github.com/google/digitalbuildings/'
GITHUB_LICENSE = GITHUB + 'license'
