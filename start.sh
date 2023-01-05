#!/usr/bin/env sh

# download all nltk data
python -m nltk.downloader $(cat nltk.txt)

# start the server
gunicorn inscribe.wsgi --bind "0.0.0.0:${PORT}" --log-file -
