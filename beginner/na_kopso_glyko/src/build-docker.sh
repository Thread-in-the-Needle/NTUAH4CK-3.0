#!/bin/bash
docker rm -f glyko
docker build -t glyko .
docker run --name=glyko --rm -p1337:1337 -it glyko