from django import forms


class NameForm(forms.Form):
    name = forms.CharField(
        label='Name',
        required=True,
    )
    age = forms.IntegerField(
        label='Age',
        required=True,
        min_value=0,
        max_value=90
    )
