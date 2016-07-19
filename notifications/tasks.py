from __future__ import absolute_import
from .models import Token
import . import api
from celery import shared_task
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@shared_task
def check_weather_for_user(token_id):
    response = api.check_for_rain_at_location(token_id=token_id)
