#!/bin/bash
docker rm -f santas-lists
docker build -t santas-lists .
docker run --name=santas-lists --rm -p1337:80 -it santas-lists