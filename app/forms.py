# from django.forms import ModelForm
from django import forms
from .models import PostContent

    
class PostContentForm(forms.ModelForm):
    class Meta:
        model = PostContent
        fields = ['title',
        'sound',
        'text',
        'active_area',
        'mypart',
        'recruite_part',
        'genre',
        'favorite',
        'days_of_theweek',
        ]
        widgets = {
            'mypart':forms.CheckboxSelectMultiple,
            'recruite_part':forms.CheckboxSelectMultiple,
            'active_area':forms.CheckboxSelectMultiple,
            'genre':forms.CheckboxSelectMultiple,
            'days_of_theweek':forms.CheckboxSelectMultiple,
        }





