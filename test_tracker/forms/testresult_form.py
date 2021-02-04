from django import forms
from test_tracker.models.test_result import TestResult
from bootstrap_modal_forms.forms import BSModalModelForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_datepicker_plus import DatePickerInput


class TestResultForm(BSModalModelForm):
    class Meta:
        model = TestResult
        fields = ['date', 'status', 'author', 'testcase', 'note']
