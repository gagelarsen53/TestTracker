from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.mixins import PassRequestMixin

from test_tracker.forms.product_form import ProductForm
from test_tracker.models import Product


class ProductCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create_product.html'
    form_class = ProductForm
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('index')


class ProductUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Product
    template_name = 'test_tracker/update_product.html'
    form_class = ProductForm
    success_message = 'Success: Product was updated.'
    success_url = reverse_lazy('index')
