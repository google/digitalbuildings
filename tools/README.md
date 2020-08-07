# Using Dockerized Instance Validator

We provide a Docker solution for clients to run the instance validator on any platform.

Rename your configuration file to be `building_config.yaml` and add it to the `tools/validators/instance_validator` folder.

Navigate to the `digitalbuildings` project directory then run `sudo docker build -t instance_validator_dockerized .` (with the period included).

Run the command `sudo docker run instance_validator_dockerized`.