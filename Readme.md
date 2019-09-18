# React and Flask starter app

This is a starter Flask/React app. 

## Run locally

`flask run`, after setting the FLASK_APP env variable

or 

`gunicorn server:app`


## Docker Image

Build with `make docker`.

Run and enter container with `sudo docker run -ti --entrypoint=/bin/bash natev/server:v001 -i`
