FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
curl \
xvfb \
libxi6 \
libgconf-2-4 \
libappindicator1 \
fonts-liberation \
libnss3 

RUN apt-get install -y wget gnupg \
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
&& apt-get update \
&& apt-get install -y google-chrome-stable

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_PORT=1337

RUN mkdir -p /opt/app
COPY ./app /opt/app
WORKDIR /opt/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1337

CMD ["/bin/bash","/opt/app/serve.sh"]