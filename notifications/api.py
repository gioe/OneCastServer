import logging
import json
import requests
import urllib.parse
import forecastio
from datetime import datetime
from django.db import transaction
from django.conf import settings
from django.core.exceptions import ValidationError

def check_for_rain_at_location(longitude, latitude):
    api_key = settings.FORECAST_API_KEY
    lat = latitude
    lng = longitude
    forecast = forecastio.load_forecast(api_key, lat, lng)

    for i in forecast.hourly().data:
        if ("Drizzle" in i.summary) | ("Rain" in i.summary):
            print('We have rain at time %s' % i.time)

    return forecast
