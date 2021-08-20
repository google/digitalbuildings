# Inputs/Output
# The tool should accept four sets of files, specified at the command line:
# Digital Building Ontology Ontology files (from github)
# Known good Building Configuration file
# Building Configuration to be scored
# Local type additions to DBO (in YAML, similar to the ontology)
# The tool must produce a matrix of scores along the dimensions described in scoring detail.  Output should be trivially importable into Google Sheets.
# Integration
# The new functionality should take advantage of existing code for reading and validating inputs wherever possible.

from score.score import Score

print('Let\'s get you a score…\n')

ontology = '/Users/atom/Documents/work/digitalbuildings/ontology/yaml'
solution = '/Users/atom/Documents/work/digitalbuildings/ontology/yaml'
proposed = '/Users/atom/Documents/work/digitalbuildings/ontology/yaml'
additions = '/Users/atom/Documents/work/digitalbuildings/ontology/yaml'

if __name__ == '__main__':
  Score(ontology, solution, proposed, additions)
