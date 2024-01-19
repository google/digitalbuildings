# ABEL User Guide

### What is ABEL?

ABEL, or **A**utomated **B**uilding **E**ntity **L**oader, is a tool that assists systems integrators (and other DBO users) in efficiently creating and modifying [Building Configuration YAML files](../../ontology/docs/building_config.md) through use of a [spreadsheet](./validators/README.md).

Building configuration files contain information about equipment, devices, and spaces within a building such as their device type, input and output points (fields) used to control them, and their relationship to one another. Building configuration files are onboarded in order to create a digital representation of the devices in the cloud and make use of the data coming from their associated fields. Due to the sheer size of building configuration files (a complete building configuration file for a building can contain thousands of devices with tens of thousands of fields), creating or editing one manually in YAML format can be very time consuming and prone to mistakes. ABEL streamlines this process by allowing the systems integrator to create and edit these files in a spreadsheet format to make it quicker and easier to edit multiple entities or fields at once.

ABEL has the following key features:

* Create and edit a Google Sheet (in the ABEL Spreadsheet Template) and export it to a building configuration file for onboarding.
 * Run Instance Validator (with optional telemetry validation) on the building configuration file during the conversion process to ensure there are no errors in the file prior to attempting onboarding.
* Convert a building configuration file to a Google Sheet to make edits on.


## User Guide Contents

* [Getting Started](#getting-started)
  *	[Set Up a Tooling Environment](#set-up-a-tooling-environment)
  *	[Obtain a GCP OAuth Client Credential](#obtain-a-gcp-oauth-client-credential)
* [Using ABEL](#using-abel)
  *	[General Use](#general-use)
    *	[Update your Repository Clone and Activate your Virtual Environment](#update-your-repository-clone-and-activate-your-virtual-environment)
    *	[ABEL Arguments](#abel-arguments)
  * [Updating an Existing Building](#updating-an-existing-building)
    *	[Create a Spreadsheet and Convert it to a Building Configuration File](#create-a-spreadsheet-and-convert-it-to-a-building-configuration-file)
    *	[Generate a Building Configuration File from an Existing Spreadsheet](#generate-a-building-configuration-file-from-an-existing-spreadsheet)
  * [Initializing a New Building](#initializing-a-new-building)


## Getting Started

ABEL is a Python tool that must be run in the command line. Before starting the setup and installation process outlined below, please ensure that the following dependencies are met:

* You are running Python 3.9 or higher
* You have a local clone of the Digital Buildings repository downloaded on your computer
  * A local clone can be created by running the following in your CLI:
    
    ```
    git clone https://github.com/google/digitalbuildings.git
    ```

The following steps only need to be done on initial setup. Any steps that must be repeated with use will be outlined in the [Using ABEL](#using-abel) section.


### Set Up a Tooling Environment

A virtual tooling environment ([venv](https://docs.python.org/3/library/venv.html)) must be made to create a separate, isolated instance of the Python runtime for a project, with its own packages. To create this environment, follow the following steps:

1. In the command line, navigate to the Digital Buildings tooling library cloned on your computer. If the Digital Buildings repository is not in your home directory, replace “~” with the folder it exists within.
```
cd ~/digitalbuildings/tools/
```

2. Create a virtual environment with an environment name of your choice, in this example the environment is named “tooling.”
```
python3 -m venv tooling
```


### Obtain a GCP OAuth Client Credential

Contact your IoT Technical Program Manager and ask for an OAuth client credential.json file for authenticating against Google Sheets API. Use the credential.json file for ABEL's --credential command line argument discussed in the [ABEL Arguments](#abel-arguments) section below.


## Using ABEL

When using ABEL there is a set of commands that should be run each time to ensure that the tool and all its requirements are up to date within your local repository. These instructions can be found in the [General Use](#general-use) section. The actual command to run ABEL will use a different set of arguments depending on the action being performed. Please go to the section for the action you are trying to perform to see instructions on which [arguments](#abel-arguments) to pass in.


### General Use

This section describes commands that should be run every time ABEL is used to make sure the program and validation are up to date, as well as an overview of all of the arguments possible to pass into ABEL.


#### Update your Repository Clone and Activate your Virtual Environment

The following commands will make sure the Digital Buildings repository as a whole is up to date, that your virtual environment is active, and that you have the most up to date packages installed for ABEL:

1. In the command line, navigate to the Digital Buildings repository cloned on your computer. If the Digital Buildings repository is not in your home directory, replace “~” with the folder it exists within.
  ```
  cd ~/digitalbuildings/
  ```

2. Pull any updates made to the repository since your last pull.
  ```
  git pull
  ```

3. Navigate to the tools folder where your virtual environment was created. 
  ```
  cd /tools/
  ```

4. Activate your virtual environment. Replace “tooling” with the name you gave your venv. 

    * MacOs/Linux:
      ```
      source tooling/bin/activate
      ```
  
   * Windows:
      ```
      tooling\Scripts\activate
      ```

5. Configure dependencies/packages.

    * MacOs/Linux:
      ```
      ./pip_install.sh
      ```
  
    * Windows:
      ```
      pip_install.bat
      ```

6. Navigate to the ABEL directory.

    * MacOs/Linux:
      ```
      cd abel
      ```
  
    * Windows:
      ```
      cd /abel/
      ```

7. Continue to whichever section below matches the action you are trying to perform and follow the instructions provided.


#### ABEL Arguments

Below is a list of all arguments that can be passed into abel. Some of these are required for any ABEL process whereas others are only required for some. The task-based instructions provided in the following three sections will show which arguments you need for your desired action.

| Argument  | Requirement | Description |
| ------------- | ------------- | ------------- |
| -c or --credential  | Always Required  | The absolute or relative path to a [GCP OAuth client credential JSON file](#obtain-a-gcp-oauth-client-credential). An OAuth client credential is required for authentication against Google Sheets service.  |
| -s or --spreadsheet_id  | Required for Certain Workflows  | The ID associated with a Google Sheets spreadsheet. A Google Sheets ID is found embedded into the spreadsheet's URL (e.g., https://docs/google/com/spreadsheets/d/<spreadsheet_id>/edit#gid=123467). This is required when ABEL is creating a building configuration YAML file from a Google spreadsheet.  |
| -b or --building_config  | Required for Certain Workflows  | The absolute or relative file path to a local building configuration file (YAML file on the system integrator’s computer). Only required for when able is making a spreadsheet from a building configuration file.  |
| -p or --subscription  | Optional  | A fully-qualified path to a Google Cloud Pubsub subscription, e.g., projects/google.com:your-project/subscriptions/your-subscription. This parameter is only required if telemetry validation is desired during the building configuration generation.  |
| -o or --timeout  | Optional  | Custom timeout duration in seconds for the telemetry validation test. The default value is 600 seconds, or 10 minutes. If this time limit is exceeded before the validator receives a test pubsub message for each of the entities configured in the given building configuration file, the test will fail with an error and report the entities that were not heard from.  |
| -m or --modified-types-filepath  | Optional  | A fully-qualified path to a modified ontology that is not in the Digital Buildings repository. The Ontology Validator will surface validation results from the modified ontology, and building configuration files will be validated against the modified ontology. This should be used to validate against ontology edits/additions the system’s integrator has made that have not had approved pull requests. Note that the building configuration must pass validation against the ontology in the Digital Buildings repository before the file can be considered ready to onboard.  |
| -d or --output-dir  | Optional  | An absolute or relative file path to a directory which ABEL can write files to. ABEL must have write access to this directory or else an error will be raised. If not provided, ABEL will write files to the current directory by default.  |


### Updating an Existing Building

Use the directions in this section when you would like to update or add entities for a building that has already been onboarded itself. Make sure you have completed the steps in the [General Use](#general-use) section before continuing to any of the steps below. 

During the conversion of the ABEL spreadsheet to a building configuration YAML file, if your spreadsheet does not pass validation then ABEL will fast-fail and a validation report will be created in the current or specified directory with the name “spreadsheet_validation_<todays_date_and_time>.log”. If the spreadsheet does pass validation then the resulting building configuration file and instance validation report will be written to the current or specified directory with the following names accordingly: “bc_export_<today_date_and_time>.yaml” and 
“instance_validation_<today_date_and_time>.log”.


#### Create a Spreadsheet and Convert it to a Building Configuration File

Use the commands below if you do not have an ABEL spreadsheet already created for the entities you would like to onboard. This process will generate a spreadsheet template for you to fill out, then allow you to convert that spreadsheet into a building configuration YAML file once completed. 

Because the building already exists in the cloud, this process requires an initial building configuration file to be passed in for editing in spreadsheet format. Export the configuration file for the building or specific for entities prior to following the steps below. 

1. Run the ABEL command with the arguments provided. Note that the arguments in brackets are optional. See the [ABEL Arguments](#abel-arguments) section for details.
```
python3 abel.py -c </path/to/credential.json> -b <absolute/path/to/building/config>
[-p  <projects/google.com:your-project/subscriptions/your-subscription>] [-o <300>] [-m </path/to/ontology]
[-d /path/to/desired/output/directory>]
```

2. Select ```option 1```, modify a spreadsheet/building config for an existing building, by entering a “1” into the command prompt. This indicates that you are working with an already onboarded building.


3. Select ```option 1```, edit or update an existing building config, by entering a “1” into the command prompt.This indicates that you do not have an existing spreadsheet and would like to create one off of an initial building configuration file. Note that the building configuration file’s metadata is set to update or initialize for this step to be successful.


4. Make any edits or additions to the building entities using the ABEL spreadsheet generated.


5. Return to the command prompt when finished and press any key to perform validation and generate a new building configuration YAML file.


#### Generate a Building Configuration File from an Existing Spreadsheet

Use the commands below if you have already created and edited an ABEL spreadsheet for the entities you would like to onboard. This process will convert your edited spreadsheet into a building configuration YAML file. 

1. Run the ABEL command with the arguments provided. Note that the arguments in brackets are optional. See the [ABEL Arguments](#abel-arguments) section for details.
```
python3 abel.py -s <input_spreadsheet_id>  -c </path/to/credential.json>
[-p  <projects/google.com:your-project/subscriptions/your-subscription>] [-o <300>] [-m </path/to/ontology>]
[-d </path/to/desired/output/directory>]
```

2. Select ```option 1```, modify a spreadsheet/building config for an existing building, by entering a “1” into the command prompt. This indicates that you are working with an already onboarded building.


3. Select ```option 2```, create building config from an updated spreadsheet, by entering a “2” into the command prompt. This indicates that you have already created and edited an ABEL spreadsheet and would like to convert it to a building configuration file. Selecting this option will initialize validation and generate a building configuration YAML file.


### Initializing a New Building

Use the directions in this section when you would like to add entities for a building that has not yet been onboarded itself. Make sure you have completed the steps in the [General Use](#general-use) section before continuing to any of the steps below. 

During the conversion of the ABEL spreadsheet to a building configuration YAML file, if your spreadsheet does not pass validation then ABEL will fast-fail and a validation report will be created in the current or specified directory with the name “spreadsheet_validation_<todays_date_and_time>.log”. If the spreadsheet does pass validation then the resulting building configuration file and instance validation report will be written to the current or specified directory with the following names accordingly: “bc_export_<today_date_and_time>.yaml” and 
“instance_validation_<today_date_and_time>.log”.

Note that because the building does not exist in the cloud, there is no option to generate a spreadsheet off of an initial building configuration file as in the [Create a Spreadsheet then Convert it to a Building Configuration File](#create-a-spreadsheet-then-convert-it-to-a-building-configuration-file) section for existing buildings. The spreadsheet template must be manually copied instead as shown in step one below.

1. Create a spreadsheet for ABEL from the [ABEL Spreadsheet template](https://docs.google.com/spreadsheets/d/1b6IRimNS1dAtPjkNN-fk4TirnLzOiDyyUmOKP_MhMM0/copy#gid=980240783) by following the link and clicking “Make a copy”.

2. Populate your spreadsheet. A well-defined guide on how to populate your spreadsheet can be found in the [spreadsheet docs](https://github.com/google/digitalbuildings/blob/master/tools/abel/validators/README.md).

3. Run the ABEL command with the arguments provided. Note that the arguments in brackets are optional. See the [ABEL Arguments](#abel-arguments) section for details.
```
python3 abel.py -s <input_spreadsheet_id>  -c </path/to/credential.json>
[-p  <projects/google.com:your-project/subscriptions/your-subscription>] [-o <300>] [-m </path/to/ontology>]
[-d </path/to/desired/output/directory>]
```

4. Choose ```option 2```, create a spreadsheet for a new building, by entering a “2” into the command prompt. This indicates that you are working with a new building and would like to convert a newly created spreadsheet into a building configuration file. Selecting this option will initialize validation and generate a building configuration YAML file.
