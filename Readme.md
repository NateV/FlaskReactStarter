# React and Flask starter app

This is a starter Flask/React app. 

## Run locally

`flask run`, after setting the FLASK_APP env variable

or 

`gunicorn clsreporter:app`


## Docker Image

Build with `make docker`.

Run and enter container with `sudo docker run -ti --entrypoint=/bin/bash natev/clsreporter:v001 -i`
