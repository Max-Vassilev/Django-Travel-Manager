from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FinalProject.common.urls')),
    path('accounts/', include('FinalProject.accounts.urls')),
    path('trips/', include('FinalProject.trips.urls')),
    path('destinations/', include('FinalProject.destinations.urls')),
]
