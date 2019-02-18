from django import forms


class UploadTestCasesForm(forms.Form):
    results_file = forms.FileField()
