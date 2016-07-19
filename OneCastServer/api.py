import json
from django.contrib.auth.models import User
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from notifications.models import Token
from tastypie.authorization import Authorization

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

    def obj_create(self,bundle,**kwargs):
        bundle = super(TokenResource,self).obj_create(bundle,**kwargs)

        # Add code here

        return bundle
