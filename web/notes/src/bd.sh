#!/bin/bash
docker rm -f notes
docker build -t notes .
docker run --name=notes --rm -p1337:1337 -it notes