# Dockerfile for instance validator, docs available at
# tools/validators/instance_validator/README.md

FROM python:3
COPY ./ ./
ENV PYTHONPATH ./
RUN pip install certifi
RUN python ./rdf_generator/setup.py install
RUN python ./validators/instance_validator/setup.py install
RUN python ./validators/ontology_validator/setup.py install
CMD ["python", "./validators/instance_validator/instance_validator.py", "-i", "building_config.yaml"]