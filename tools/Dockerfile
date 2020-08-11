# Dockerfile for instance validator, docs available at
# tools/validators/instance_validator/README.md

FROM python:3.8-slim-buster
COPY ./ ./
ENV PYTHONPATH ./
RUN python ./rdf_generator/setup.py install
RUN python ./validators/instance_validator/setup.py install
RUN python ./validators/ontology_validator/setup.py install
WORKDIR ./validators/instance_validator
CMD ["python", "instance_validator.py", "-i", "building_config.yaml"]