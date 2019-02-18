from django import forms
from test_tracker.models.test_subcategory import TestSubcategory
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TestSubcategoryForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = TestSubcategory
        fields = ['subcategory', 'description']
