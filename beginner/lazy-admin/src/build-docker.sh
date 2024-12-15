#!/bin/bash
docker rm -f lazy-admin
docker build -t lazy-admin .
docker run --name=lazy-admin --rm -p1337:1337 -it lazy-admin 