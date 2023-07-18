from django import forms
from FinalProject.trips.models import VisitedPlace


class AddEditTripForm(forms.ModelForm):
    class Meta:
        model = VisitedPlace
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
