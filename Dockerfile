FROM python:alpine3.8
LABEL MAINTAINER="Haseeb Majid hello@haseebmajid.dev"

COPY dist ./dist/
RUN pip install dist/*
