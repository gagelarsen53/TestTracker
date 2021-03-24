from django import forms
from django.contrib.auth.models import User

from test_tracker.models.product import Product
from test_tracker.models.test_case import TestCase
from test_tracker.models.test_category import TestCategory
from test_tracker.models.test_subcategory import TestSubcategory

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class TestCaseForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['product', 'name', 'source', 'summary', 'category', 'subcategory',
                  'active', 'needs_review', 'create_date', 'author']

    def __init__(self, *args, **kwargs):
        super(TestCaseForm, self).__init__(*args, **kwargs)

        all_products = Product.objects.all().order_by('name')
        products = [(product.id, f'{product.name}-{product.version}') for product in all_products]
        self.fields['product'].choices = products

        all_categories = TestCategory.objects.all().order_by('category')
        categories = [(category.id, category.category) for category in all_categories]
        self.fields['category'].choices = categories

        all_subcategories = TestSubcategory.objects.all().order_by('subcategory')
        subcategories = [(subcategory.id, subcategory.subcategory) for subcategory in all_subcategories]
        self.fields['subcategory'].choices = subcategories

        users = User.objects.all().order_by('username')
        authors = [(user.id, user.username) for user in users]
        self.fields['author'].choices = authors
