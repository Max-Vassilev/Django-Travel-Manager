from django.urls import path
from FinalProject.trips.views import *

urlpatterns = [
    path('add/', TripAddView.as_view(), name='add trip'),
    path('delete/<int:pk>/', trip_delete, name='delete trip'),
    path('edit/<int:pk>/', trip_edit, name='edit trip'),
    path('visited_places/<int:pk>/', VisitedPlacesView.as_view(), name="visited places"),
]
