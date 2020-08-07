# Dockerfile for instance validator, docs available at
# tools/validators/instance_validator/README.md

FROM python:3
COPY ./ ./
ENV PYTHONPATH ./
WORKDIR ./tools/validators/instance_validator
RUN pip install strictyaml
RUN pip install absl-py
RUN pip install pyglib 
RUN pip install pyyaml 
CMD ["python", "instance_validator.py", "-i", "config.yaml"]