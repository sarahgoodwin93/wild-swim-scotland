from django import forms
from .models import SwimPosts, Review


class AddSwimForm(forms.ModelForm):
    """
    FORM: Add Swim.
    """
    title = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "title-field"}),
        label="Swim Title",
    )
    