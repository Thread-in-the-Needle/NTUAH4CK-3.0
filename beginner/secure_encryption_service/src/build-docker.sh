#!/bin/bash
docker rm -f sec
docker build -t sec .
docker run --name=sec --rm -p1337:1337 -it sec