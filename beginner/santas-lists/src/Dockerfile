FROM php:7.4-apache

# set environment variables
ENV APP_PORT=80

COPY ./app /var/www/html/

COPY secret.php /secret.php

WORKDIR /var/www/html/

EXPOSE 80

# Start the Apache server
CMD ["/bin/bash","serve.sh"]