#!/bin/bash
docker rm -f pinger
docker build -t pinger .
docker run --name=pinger --rm -p1337:1337 -it pinger 