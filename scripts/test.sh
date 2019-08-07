#!/usr/bin/env bash
set -x
set -e

DOCKER_IMAGE=secret-injector
docker build . -t $DOCKER_IMAGE
exec docker run --rm $DOCKER_IMAGE:latest

