#!/bin/bash
docker rm -f babyprison
docker build -t babyprison .
docker run --name=babyprison --rm -p1337:1337 -it babyprison