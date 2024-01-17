from django import forms
from .models import SwimPosts, Review


class AddSwimForm(forms.ModelForm):
    """
    FORM: Add Swim.
    """
    class Meta:
        model = SwimPosts
        fields = ['title', 'description', 'date', 'time', 'location', 'post_image']


class ReviewForm(forms.ModelForm):
    """
    FORM: Review.
    """

    class Meta:
        model = Review
        fields = [
            "review",
        ]
    review = forms.CharField(widget=forms.Textarea, label="Write a Review")
