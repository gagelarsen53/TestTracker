from django import forms
from test_tracker.models.test_category import TestCategory
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TestCategoryForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = TestCategory
        fields = ['category', 'description']
