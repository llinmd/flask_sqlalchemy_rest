FROM python:3.9-slim-buster

USER root

# set the working directory in the container
WORKDIR /opt/app-root/

EXPOSE 5000

COPY requirements.txt .

# install dependencies
RUN pip install -r /opt/app-root/requirements.txt

# copy files to the working directory
COPY *.py *.ini .

USER 1001

# command to run on containerdoc start
CMD [ "python", "./app.py" ]
