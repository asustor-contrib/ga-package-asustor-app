FROM python:2.7.18-slim-buster

ENV PYTHONUNBUFFERED "1"
ENV PYTHONIOENCODING "utf-8"

WORKDIR /github/workspace

ADD apkg_tools.py /usr/src/app/apkg_tools.py
ADD entrypoint.py /usr/src/app/entrypoint.py

ENTRYPOINT ["/usr/src/app/entrypoint.py"]
