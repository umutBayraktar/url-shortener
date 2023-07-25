FROM python:3.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN chmod +x /code/docker/scripts/entrypoint.sh
ENTRYPOINT ["/code/docker/scripts/entrypoint.sh"]
