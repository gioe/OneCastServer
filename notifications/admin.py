from django.contrib import admin
from .models import Token
from kombu.transport.django import models as kombu_models

class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_token', 'zip_code', 'notification_time']

admin.site.register(Token, TokenAdmin)
admin.site.register(kombu_models.Message)
# Register your models here.
