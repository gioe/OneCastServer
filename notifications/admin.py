from django.contrib import admin

from .models import Token

class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_token', 'zip_code', 'notification_time']

admin.site.register(Token, TokenAdmin)
# Register your models here.
