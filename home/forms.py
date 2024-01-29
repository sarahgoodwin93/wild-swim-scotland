from django import forms
from .models import SwimPosts, Review


class AddSwimForm(forms.ModelForm):
    """
    FORM: Add Swim.
    """
    class Meta:
        model = SwimPosts
        fields = ['title', 'description', 'date', 'time',
                  'swim_difficulty', 'location', 'post_image']


class EditSwimForm(forms.ModelForm):
    """
    FORM: Edit Swim.
    """
    class Meta:
        model = SwimPosts
        fields = ['title', 'description', 'date', 'time',
                  'swim_difficulty', 'location', 'post_image']


class ReviewForm(forms.ModelForm):
    """
    FORM: Review.
    """

    class Meta:
        model = Review
        fields = ['review_title', 'review_location', 'body']
