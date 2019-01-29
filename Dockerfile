FROM python:latest
MAINTAINER Bruno Thalmann

WORKDIR /
COPY docker_entrypoint.sh /
RUN chmod +x docker_entrypoint.sh

WORKDIR /app
COPY . /app
ENTRYPOINT ["/docker_entrypoint.sh"]