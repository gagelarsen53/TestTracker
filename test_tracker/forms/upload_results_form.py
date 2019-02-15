import datetime

from django import forms


class UploadResultsForm(forms.Form):
    date_of_results = forms.DateField(
        initial=datetime.date.today,
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    results_file = forms.FileField()
