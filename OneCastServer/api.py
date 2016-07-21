import json
from datetime import datetime, timedelta
from tzlocal import get_localzone
from push_notifications.models import APNSDevice
from django.contrib.auth.models import User
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from notifications.models import Token
from tastypie.authorization import Authorization
from notifications.tasks import check_weather_for_user

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class TokenResource(ModelResource):
    class Meta:
        queryset = Token.objects.all()
        resource_name = 'token'
        authorization = Authorization()
        serializer = Serializer()
        always_return_data = True

    def obj_create(self, bundle, request=None, **kwargs):
        bundle = super(TokenResource, self).obj_create(bundle, request=request, **kwargs)
        if bundle.data['device_token']:
            device, created = APNSDevice.objects.get_or_create(registration_id=bundle.data['device_token'])
            if created:
                device.save
                date_object = datetime.strptime(bundle.data['notification_time'], '%H:%M:%S')
                time = date_object.time()
                local_zone = get_localzone()
                today_date =  datetime.today()
                combination = datetime.combine(today_date, time)
                eta = local_zone.localize(combination)
                device_token=bundle.data['device_token']
                check_weather_for_user.apply_async((device_token,), eta=eta)

        return bundle

    def obj_update(self, bundle, request=None, **kwargs):
        bundle = super(TokenResource, self).obj_create(bundle, request=request, **kwargs)
        if bundle.data['device_token']:
            device, created = APNSDevice.objects.get_or_create(registration_id=bundle.data['device_token'])
            if created:
                device.save
        return bundle
