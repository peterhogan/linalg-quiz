FROM python:3-onbuild

RUN apt-get update -y && apt-get install -y texlive-full;
