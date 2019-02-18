from django import forms
from test_tracker.models.test_status import TestStatus
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TestStatusForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = TestStatus
        fields = ['status', 'hex_color', 'text_hex_color']
