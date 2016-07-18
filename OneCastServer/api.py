import json
from tastypie.serializers import Serializer
from tastypie.resources import ModelResource
from notifications.models import User
from tastypie.authorization import Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        serializer = Serializer()

    def obj_create(self,bundle,**kwargs):
        bundle = super(UserResource,self).obj_create(bundle,**kwargs)

        # Add code here

        return bundle
