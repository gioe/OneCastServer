import logging
import json
import requests
import urllib.parse
import forecastio
import pytz, datetime
from notifications import models
from django.db import transaction
from django.conf import settings
from django.core.exceptions import ValidationError

def check_for_rain_at_location(token_id):
    current_user = models.Token.objects.get(id=token_id)
    api_key = settings.FORECAST_API_KEY
    lat = current_user.location_latitude
    lng = current_user.location_longitude
    forecast = forecastio.load_forecast(api_key, lat, lng)

    for i in forecast.hourly().data:
        if ("Drizzle" in i.summary) | ("Rain" in i.summary):
            print('We have rain at time %s' % i.time)

    return forecast
