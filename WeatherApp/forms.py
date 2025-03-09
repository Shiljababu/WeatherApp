from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label = "Enter your name", max_length = 100, widget = forms.TextInput(attrs = {
        'class':'form-control',
        'placeholder':'City Name',
    }))