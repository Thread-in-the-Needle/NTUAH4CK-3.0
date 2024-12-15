#!/bin/sh

mv flag.txt flag-$(head -c 32 /dev/urandom | sha1sum | cut -d ' ' -f 1).txt

node index.js