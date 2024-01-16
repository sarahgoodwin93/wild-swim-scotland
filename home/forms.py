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
    description = forms.TextField(
        widget=forms.HiddenInput(attrs={"id": "description-field"}),
        label="Description",
    )
    date = forms.DateField(
        widget=forms.HiddenInput(attrs={"id": "date-field"}),
        label="Date",
    )
    time = forms.TimeField(
        widget=forms.HiddenInput(attrs={"id": "time-field"}),
        label="Time",
    )
    location = forms.TextField(
        widget=forms.HiddenInput(attrs={"id": "location-field"}),
        label="Location",
    )

    class Meta:
        model = SwimPosts
        fields = [
            "title", "description", "date", "time", "location"
        ]


class ReviewForm(forms.ModelForm):
    """
    FORM: Add Swim.
    """

    class Meta:
        model = Review
        fields = [
            "review",
        ]
    
    review = forms.CharField(widget=forms.Textarea, label="Write a Review")