from django.urls import path
from FinalProject.destinations.views import *

urlpatterns = [
    path('dream_destinations/<int:pk>/', DreamDestinationsView.as_view(), name="dream destinations"),
    path('add/', DestinationAddView.as_view(), name='add destination'),
    path('delete/<int:pk>/', destination_delete, name='delete destination'),
    path('edit/<int:pk>/', destination_edit, name='edit destination'),
    path('i_went_there/<int:pk>/', i_went_there_view, name='i went there'),
]

