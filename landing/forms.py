from django import forms

class SearchForm(forms.Form):
    keywords = forms.CharField()
    property_type = forms.CharField()
