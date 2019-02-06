from django import forms
from test_tracker.models.product import Product
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class ProductForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'version', 'notes']
