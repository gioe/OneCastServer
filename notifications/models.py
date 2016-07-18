from django.db import models
from django.utils.translation import gettext as _

class User(models.Model):
    device_token = models.CharField("Token", blank=True, null=True, max_length=255)
    zip_code = models.CharField("Zip Code", max_length=255, blank=True, null=True)
    notification_time = models.TimeField("Notification Time", blank=True)
    location_latitude = models.FloatField("Latitude", blank=True, null=True)
    location_longitude = models.FloatField("Longtitude", blank=True, null=True)

    def __str__(self):
        return self.device_token
