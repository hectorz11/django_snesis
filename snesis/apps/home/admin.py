from django.contrib import admin
from snesis.apps.home.models import UserProfile,Backup

admin.site.register(UserProfile)
admin.site.register(Backup)