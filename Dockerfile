FROM python:3.5.2

MAINTAINER Kristoffer Dalby


ENV NAME=shiny-octo-shame

ENV DIR=/srv/app

RUN mkdir $DIR
WORKDIR $DIR

# Install requirements
COPY ./req.txt $DIR/req.txt
RUN pip install -r req.txt --upgrade

# Copy project files
COPY . $DIR

EXPOSE 8080
EXPOSE 8081

CMD ["sh", "docker-entrypoint.sh"]
