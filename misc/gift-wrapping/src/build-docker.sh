#!/bin/bash
docker rm -f gift
docker build -t gift .
docker run --name=gift --rm -p1337:1337 -it gift