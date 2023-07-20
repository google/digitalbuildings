FROM python:3.9
WORKDIR /source
COPY . /source
RUN /source/tools/scripts/docker_setup.sh
WORKDIR /work
ENTRYPOINT ["/source/tools/scripts/docker_entry.sh"]
