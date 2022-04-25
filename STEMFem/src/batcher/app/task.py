from __future__ import absolute_import
from app.celeryapp import app
import time
import requests
import json
import os

@app.task
def addmentor(name, profession, availability):
    payload = {"name": name, "profession": profession, "availability": availability} 
    try:
        upload = requests.post('http://FE:5000/event', json=payload, timeout=60)
    except Exception as err:
        raise f'Error occurred: {err}'
    return 'Mentor uploaded'


@app.task
def addmentee(name, grade, availability):
    payload = {"name": name, "grade": grade, "availability": availability}
    try:
        upload = requests.post('http://FE:5000/event', json=payload, timeout=60)
    except Exception as err:
        raise f'Error occurred: {err}'
    return 'Mentee uploaded'
