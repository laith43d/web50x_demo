from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(
        label='Task title',
        required=True,
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        label='Task Date',
        required=False,
    )
    priority = forms.IntegerField(
        widget=forms.NumberInput(attrs={'step': '500'}),
        label='Priority',
        required=False,
    )
