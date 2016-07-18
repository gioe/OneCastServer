from django.db import models
from django.utils.translation import gettext as _

class User(models.Model):
    device_token = models.CharField(blank=True, null=True, max_length=255)
    zip_code = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Zip Code'))
    notification_time = models.TimeField(_(u"Notification Time"), blank=True)
    location_latitude = models.FloatField("Latitude", blank=True, null=True)
    location_longitude = models.FloatField("Longtitude", blank=True, null=True)

    def __str__(self):
        return self.device_token

# Create your models here.
