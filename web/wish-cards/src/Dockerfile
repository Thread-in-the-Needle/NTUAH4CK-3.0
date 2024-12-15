FROM python:3.9-slim

RUN apt update && apt install -y wkhtmltopdf


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