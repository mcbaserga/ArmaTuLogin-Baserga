from django.contrib import admin

# Register your models here.

from .models import Profile, Blog

admin.site.register(Profile)
admin.site.register(Blog)