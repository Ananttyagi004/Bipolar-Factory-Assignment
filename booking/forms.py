from django import forms
from .models import Flight, Booking

class FlightSearchForm(forms.Form):
    departure_city = forms.CharField(max_length=100, required=False)
    arrival_city = forms.CharField(max_length=100, required=False)
    departure_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flight']