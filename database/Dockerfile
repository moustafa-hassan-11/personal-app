#######
# Database Dockerfile
#

FROM mysql
LABEL version="1.0" \
description="This is mysql container image" \
creationDate="22-07-02" \
author="Moustafa Youssef"

MAINTAINER moustafayoussef759@gmail.com

ENV MYSQL_ROOT_PASSWORD="PASSWORD"

EXPOSE 3306
ADD schema.sql /docker-entrypoint-initdb.d
#user 1002

