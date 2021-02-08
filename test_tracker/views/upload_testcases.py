"""
********************************************************************************
* Name: upload_testcases.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.forms.upload_testcases_form import UploadTestCasesForm
from test_tracker.models.test_case import TestCase


@login_required
@transaction.atomic
def upload_testcases(request, name, version):
    context = {}
    products = Product.objects.filter(active=True).order_by("name")
    context['products'] = products
    product = Product.objects.get(name=name, version=version)

    author = request.user

    context['product'] = product
    context['author'] = author
    context['post_data'] = False

    if request.method == 'POST':
        form = UploadTestCasesForm(request.POST, request.FILES)
        if form.is_valid():
            context['post_data'] = True
            testcases, errors = TestCase.test_cases_from_json_file(request.FILES['results_file'])

            context['success'] = len(testcases)
            for testcase in testcases:
                testcase.save()

            if len(errors) > 0:
                context['errors'] = errors
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            context['errors'] = ['Invalid/missing form entries...']
    else:
        form = UploadTestCasesForm()

    context['form'] = form

    return render(request, "test_tracker/upload_testcases.html", context)
