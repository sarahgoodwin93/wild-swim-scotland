from django import forms
from .models import SwimPosts
from datetime import date


class AddSwimForm(forms.ModelForm):
    """
    FORM: Add Swim.
    """

    class Meta:
        model = SwimPosts
        fields = [
            "title",
            "description",
            "date",
            "time",
            "swim_difficulty",
            "location",
            "post_image",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "placeholder": "yyyy-mm-dd"}
            ),
            "time": forms.TimeInput(attrs={"placeholder": "00:00:00"}),
        }


class EditSwimForm(forms.ModelForm):
    """
    FORM: Edit Swim.
    """

    class Meta:
        model = SwimPosts
        fields = [
            "title",
            "description",
            "date",
            "time",
            "swim_difficulty",
            "location",
            "post_image",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "placeholder": "yyyy-mm-dd"}
            ),
            "time": forms.TimeInput(attrs={"placeholder": "00:00:00"}),
        }