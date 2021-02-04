from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from bootstrap_modal_forms.mixins import PassRequestMixin
from bootstrap_modal_forms.generic import BSModalUpdateView

from test_tracker.forms.product_form import ProductForm
from test_tracker.forms.testcase_form import TestCaseForm
from test_tracker.forms.testresult_form import TestResultForm
from test_tracker.forms.testcatgory_form import TestCategoryForm
from test_tracker.forms.testsubcategory_form import TestSubcategoryForm
from test_tracker.forms.teststatus_from import TestStatusForm

from test_tracker.models import Product
from test_tracker.models import TestCase
from test_tracker.models import TestResult


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


class ProductDeleteView(PassRequestMixin, SuccessMessageMixin, generic.DeleteView):
    model = Product
    template_name = 'test_tracker/delete.html'
    success_message = 'Success: Product was deleted.'
    success_url = reverse_lazy('index')


class BaseDuplicateView(generic.edit.ModelFormMixin, generic.edit.ProcessFormView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        current_product_id = kwargs['pk']
        new_product = request._post
        all_products = Product.objects.all()

        # Verify that the product does not exist
        for product in all_products:
            if new_product['name'] == product.name and new_product['version'] == product.version:  # Already exists
                return redirect('index')

        # Create the new Product
        p = Product(name=new_product['name'], version=new_product['version'], notes=new_product['notes'])
        p.save()

        # Copy all TestCases for new Product
        current_testcases = TestCase.objects.filter(product_id=current_product_id)
        for testcase in current_testcases:
            tc = TestCase(
                name=testcase.name,
                source=testcase.source,
                summary=testcase.summary,
                active=testcase.active,
                needs_review=testcase.needs_review,
                create_date=testcase.create_date,
                author=testcase.author,
                category=testcase.category,
                product=p,
                subcategory=testcase.subcategory
            )
            tc.save()

        return redirect('index')


class DuplicateView(generic.detail.SingleObjectTemplateResponseMixin, BaseDuplicateView):
    """View for duplicating an object, with a response rendered by a template."""
    template_name_suffix = '_form'


class ProductDuplicateView(PassRequestMixin, SuccessMessageMixin, DuplicateView):
    model = Product
    template_name = 'test_tracker/duplicate.html'
    form_class = ProductForm
    success_message = 'Success: Product was duplicated.'
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


class TestCaseDeleteView(PassRequestMixin, SuccessMessageMixin, generic.DeleteView):
    model = TestCase
    template_name = 'test_tracker/delete.html'

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


class TestResultUpdateView(BSModalUpdateView):
    template_name = 'test_tracker/update.html'
    model = TestResult
    form_class = TestResultForm
    success_message = 'Success: TestResult was updated.'

    def get_success_url(self):
        product = self.get_context_data()['testresult'].testcase.product
        return reverse_lazy('dashboard', kwargs={
            'name': product.name,
            'version': product.version,
        })

    def get_object(self, queryset=None):
        hook = super(TestResultUpdateView, self).get_object(queryset)
        hook.author = self.request.user
        return hook
        

class TestResultDeleteView(PassRequestMixin, SuccessMessageMixin, generic.DeleteView):
    model = TestResult
    template_name = 'test_tracker/delete.html'

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


