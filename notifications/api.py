import logging
import json
import requests
import urllib.parse
import forecastio
import pytz, datetime
from push_notifications.models import APNSDevice
from notifications import models
from django.db import transaction
from django.conf import settings
from django.core.exceptions import ValidationError

def check_for_rain_at_location(device_token):
    current_user = models.Token.objects.get(device_token=device_token)
    device = APNSDevice.objects.get(registration_id=device_token)
    api_key = settings.FORECAST_API_KEY
    lat = current_user.location_latitude
    lng = current_user.location_longitude
    forecast = forecastio.load_forecast(api_key, lat, lng)
    forecast_timezone = forecast.json['timezone']
    time_list = []
    for i in forecast.hourly().data:
        if ("Drizzle" in i.summary) | ("Rain" in i.summary):
            time_zone = pytz.timezone(forecast_timezone)
            local_time = time_zone.localize(i.time)
            if datetime.date.today() == local_time:
                time_list.append(local_time.time())
                print('It will rain on at %s' % local_time.time())
            else:
                print ('No rain today. It with rain on %s' % local_time.date())

    if not time_list:
        device.send_message("It's not going to rain today. Leave the umbrella at home.")
    else:
        device.send_message("It's going to rain today! Bring an umbrella!")
