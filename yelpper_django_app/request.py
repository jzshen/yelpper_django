from django import forms

class RequestForm(forms.Form):
    distance = forms.CharField()
    prices = forms.CharField()
    uberType = forms.CharField()

