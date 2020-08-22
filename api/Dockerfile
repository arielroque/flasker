
FROM python:3.6.8-alpine3.9

LABEL maintainer="ariel roque"

# Install python3
RUN apk update \
  && apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
     apk add --no-cache --update python3 && \
     pip3 install --upgrade pip setuptools

# Add and install requeriments 
ADD requirements.txt /  

RUN pip3 install -r requirements.txt

# Add service
ADD . /api

WORKDIR /api

CMD ["python3","api.py"]


