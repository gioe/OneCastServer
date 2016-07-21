from __future__ import absolute_import
from .models import Token
from . import api
from celery import task
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@task()
def check_weather_for_user(device_token):
    api.check_for_rain_at_location(device_token=device_token)
