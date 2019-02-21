from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.mixins import PassRequestMixin

from test_tracker.forms.product_form import ProductForm
from test_tracker.forms.testcase_form import TestCaseForm
from test_tracker.forms.testresult_form import TestResultForm
from test_tracker.forms.testcatgory_form import TestCategoryForm
from test_tracker.forms.testsubcategory_form import TestSubcategoryForm
from test_tracker.forms.teststatus_from import TestStatusForm

from test_tracker.models import Product
from test_tracker.models import TestCase
from test_tracker.models import TestResult
from test_tracker.models import TestCategory
from test_tracker.models import TestSubcategory
from test_tracker.models import TestStatus


class ProductCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = ProductForm
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('index')


class ProductUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Product
    template_name = 'test_tracker/update.html'
    form_class = ProductForm
    success_message = 'Success: Product was updated.'
    success_url = reverse_lazy('index')


class TestCaseCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = TestCaseForm
    success_message = 'Success: TestCase was created.'

    def get_success_url(self):
        product = self.get_context_data()['testcase'].product
        return reverse_lazy('dashboard', kwargs={
            'name': product.name,
            'version': product.version,
        })


class TestCaseUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = TestCase
    template_name = 'test_tracker/update.html'
    form_class = TestCaseForm
    success_message = 'Success: TestCase was updated.'

    def get_success_url(self):
        product = self.get_context_data()['testcase'].product
        return reverse_lazy('dashboard', kwargs={
            'name': product.name,
            'version': product.version,
        })


class TestResultCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = TestResultForm
    success_message = 'Success: TestCase was created.'

    def get_success_url(self):
        product = self.get_context_data()['testresult'].testcase.product
        return reverse_lazy('dashboard', kwargs={
            'name': product.name,
            'version': product.version,
        })

    def get_initial(self):
        print(self.request)


class TestResultUpdateView(PassRequestMixin, SuccessMessageMixin, generic.UpdateView):
    model = TestResult
    template_name = 'test_tracker/update.html'
    form_class = TestResultForm
    success_message = 'Success: TestResult was updated.'

    def get_success_url(self):
        product = self.get_context_data()['testresult'].testcase.product
        return reverse_lazy('dashboard', kwargs={
            'name': product.name,
            'version': product.version,
        })


class TestCategoryCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = TestCategoryForm
    success_message = 'Success: TestCategory was created.'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')


class TestSubcategoryCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = TestSubcategoryForm
    success_message = 'Success: TestSubcategory was created.'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')


class TestStatusCreateView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'test_tracker/create.html'
    form_class = TestStatusForm
    success_message = 'Success: TestStatus was created.'

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')


