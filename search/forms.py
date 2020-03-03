from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='キーワードを入力',required=False)
