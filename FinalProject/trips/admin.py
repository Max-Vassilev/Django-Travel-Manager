from django.contrib import admin
from FinalProject.trips.models import VisitedPlace


@admin.register(VisitedPlace)
class UserModelAdmin(admin.ModelAdmin):
    pass
