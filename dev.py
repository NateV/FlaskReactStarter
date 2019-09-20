# Start up development servers.
# this requires running `npm run watch` in one process
# and flask run in another.

from multiprocessing import Process
import subprocess

def npm():
    subprocess.run("cd server/static && npm run watch", shell=True)

def flask():
    #subprocess.run("pipenv run flask run", shell=True)
    subprocess.run("pipenv run gunicorn --reload server:app", shell=True)

if __name__ == '__main__':
    npm_p = Process(target=npm)
    flask_p = Process(target=flask)
    npm_p.start()
    flask_p.start()
