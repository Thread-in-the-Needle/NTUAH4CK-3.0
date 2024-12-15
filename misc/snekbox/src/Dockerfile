FROM python:3.13-slim

RUN apt-get update && apt-get install -y socat

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY server.py .
COPY flag.txt .

EXPOSE 1337

CMD ["socat", "-v","TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 /opt/app/server.py'"]