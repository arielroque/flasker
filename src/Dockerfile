FROM python:3.6.8-alpine3.9

LABEL maintainer="ariel roque"

# Add and install requeriments 
ADD requirements.txt /  
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 5050

# Add service
ADD . /api

WORKDIR /api

CMD ["python3","api.py"]


