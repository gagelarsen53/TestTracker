from django import forms
from test_tracker.models.test_case import TestCase
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TestCaseForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['product', 'name', 'source', 'summary', 'category', 'subcategory',
                  'active', 'needs_review', 'create_date', 'author']
