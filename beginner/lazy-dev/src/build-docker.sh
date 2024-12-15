#!/bin/bash
docker rm -f lazy-dev
docker build -t lazy-dev .
docker run --name=lazy-dev --rm -p1337:1337 -it lazy-dev 