from django import forms
from FinalProject.destinations.models import DreamDestination


class AddEditDestinationForm(forms.ModelForm):
    class Meta:
        model = DreamDestination
        fields = ['location', 'place_photo']

        widgets = {
            "location": forms.TextInput(
                attrs={
                    "placeholder": "Location",
                },
            ),
            "place_photo": forms.URLInput(
                attrs={
                    "placeholder": "Link to image"
                }
            ),
        }
