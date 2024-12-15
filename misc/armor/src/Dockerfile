# set the version of python you want
FROM python:3.13

WORKDIR /app 

COPY ./src .

RUN pip install -r requirements.txt

CMD ["/bin/bash", "entrypoint.sh"]

# then docker cp the dist directory 
