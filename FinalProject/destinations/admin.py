from django.contrib import admin
from FinalProject.destinations.models import DreamDestination


@admin.register(DreamDestination)
class UserModelAdmin(admin.ModelAdmin):
    pass
