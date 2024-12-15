#!/bin/bash
docker rm -f armor
docker build -t armor .
docker run --name=armor --rm -it armor