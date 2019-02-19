import datetime

from bootstrap_datepicker_plus import DatePickerInput
from django import forms


class UploadResultsForm(forms.Form):
    results_file = forms.FileField()
    date_of_results = forms.DateField(
        initial=datetime.date.today,
        widget=DatePickerInput(format='%m/%d/%Y')
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
