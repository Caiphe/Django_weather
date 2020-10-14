from django import forms
from .models import WeatherData


class weatherForm(forms.ModelForm):
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-field',
            'placeholder': 'City',
        }))
    period = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-field',
            'placeholder': 'Period'
        }))

    class Meta:
        model = WeatherData
        fields = ['city', 'period']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].label = ''
        self.fields["period"].label = ''
