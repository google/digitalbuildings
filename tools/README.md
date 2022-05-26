# Digital Buildings Toolkit

The Digital Buildings Toolkit provides a centralized
method for interfacing with all of the tools contained within the Digital
Buildings Repository. Currently, the toolkit only supports building configuration
instance validation and guid generation, but additional funcionality will be
implemented in the future.

## Setup


### Windows Setup
1. Open cmd and navigate to `digitalbuildings/tools`
2. Run `global_setup.bat`

### Unix Setup
1. Open terminal and navigate to `digitalbuildings/tools`
2. Run `bash global_setup.sh`

## Running Toolkit

Run `python toolkit.py` and provide any of the following arguments:
- `-i/--input` for the file path or a list of file paths for building configurations
- `-g/--generate` to apply the guid generator to the input file(s)
- `-v/--validate` to apply instance validater to input file(s)
- `-m/--modified-types-filepath` file path for modified ontology
- `-s/--subscription` pubsub subscription for telemetry validation
- `-a/--service-account` Service account used to pull messages from subscription
- `-t/--timeout` Timeout duration for telemetry validation
- `-r/--report-filename` Filename for validation report

For example:
`python toolkit.py -i=//path/to/file --generate --validate -r=//path/to/report`
Takes in an input file, generates guids for every entity instance, validates the
building configuration, and writes validation results to the report filepath.

**NOTE:** For Windows, run with `py` rather than `python`
