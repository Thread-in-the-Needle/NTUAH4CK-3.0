FROM python:3.13-slim

RUN apt-get update && apt-get install -y socat

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . .

EXPOSE 1337

CMD ["/bin/bash", "serve.sh"]