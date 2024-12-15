#!/bin/bash
docker rm -f cards
docker build -t cards .
docker run --name=cards --rm -p1337:1337 -it cards 