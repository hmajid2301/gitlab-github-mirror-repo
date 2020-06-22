FROM python:alpine3.8
LABEL VERSION="0.1.1"
LABEL MAINTAINER="Haseeb Majid hello@haseebmajid.dev"

COPY dist ./dist/
RUN pip install dist/*
ENTRYPOINT [ "gitlab_github_mirror_repo" ]
