#######
# syntax=docker/dockerfile:1

FROM registry.access.redhat.com/rhscl/python-36-rhel7

LABEL version="1.0" \
description="This is Flask container image" \
creationDate="22-07-02" \
author="Moustafa Youssef"
MAINTAINER moustafayoussef759@gmail.com


ENV FLASK_APP="route" 

WORKDIR /app

COPY . /app

RUN pip install -U pip && pip3 install -r requirements.txt


user 1001

EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
