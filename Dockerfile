FROM python:3.10
WORKDIR /source
COPY . /source
WORKDIR /source/tools
RUN ./global_setup.sh
ENTRYPOINT ["/source/tools/scripts/docker-entry.sh"]
