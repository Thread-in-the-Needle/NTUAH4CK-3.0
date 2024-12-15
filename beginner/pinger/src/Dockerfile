FROM node:18

RUN apt update && apt install -y iputils-ping

RUN mkdir -p /opt/app
COPY ./app/ /opt/app
WORKDIR /opt/app
    
RUN npm install 

EXPOSE 1337

CMD ["/bin/bash","/opt/app/serve.sh"]