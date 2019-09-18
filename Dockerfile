FROM python:3.7-stretch

COPY . /srv/

WORKDIR /srv

RUN pip install pipenv && pipenv install --system && useradd -ms /bin/bash gunicorn

USER gunicorn

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--access-logfile", "-", "clsreporter:app"]