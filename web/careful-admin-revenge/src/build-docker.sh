#!/bin/bash
docker rm -f careful-admin
docker build -t careful-admin .
docker run --name=careful-admin --rm -p1337:1337 -it careful-admin