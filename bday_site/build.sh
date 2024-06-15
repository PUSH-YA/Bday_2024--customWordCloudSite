#!/usr/bin/env bash

# update env
sudo apt-get update

# install pip3
sudo apt-get install -y python3-pip

# create a virtual environment
sudo apt-get install -y python3-venv
python3 -m venv bday
source bday/bin/activate
# deactivate to deactivate the virtual environment

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files -> needed if DEBUGGING = False
# python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# runserver
python3 manage.py runserver 0.0.0.0:8000

# running locally:
# python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker