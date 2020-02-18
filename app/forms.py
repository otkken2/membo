# from django.forms import ModelForm
from django import forms
from .models import PostContent


# class SounfFileForm(forms.ModelForm):
#     class Meta:
#         model = SoundFile
#         fields = '__all__'

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
        # widgets = {
        #     'mypart':forms.CheckboxSelectMultiple,
        #     'recruite_part':forms.CheckboxSelectMultiple,
        #     'active_area':forms.CheckboxSelectMultiple,
        #     'genre':forms.CheckboxSelectMultiple
        #     }
        # labels = {
        #     'title':'タイトル',
        #     'text':'本文',
        #     'sound':'参考音源',
        #     'mypart':'投稿者のパート',
        #     'yourpart':'募集するパート',
        #     'active_area':'活動エリア（都道府県）',
        #     'genre':'ジャンル',
        #     'favorite':'好きなアーティスト'
        # }






