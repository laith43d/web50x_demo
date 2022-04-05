from django import forms

from flights.models import Flight, Passenger


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class FlightForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Date', 'autocomplete': 'off'}),
        required=True,
    )

    class Meta:
        model = Flight
        fields = [
            'origin',
            'destination',
            'date',
            'duration',
            'price',
        ]


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'first',
            'last',
            'flights',
        ]
