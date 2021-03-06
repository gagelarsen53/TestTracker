"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.forms.upload_results_form import UploadResultsForm
from test_tracker.models.test_result import TestResult


@login_required
@transaction.atomic
def upload_results(request, name, version):
    context = {}
    context['products'] = Product.objects.filter(active=True).order_by("name")
    product = Product.objects.get(name=name, version=version)

    author = request.user

    context['product'] = product
    context['author'] = author
    context['post_data'] = False

    if request.method == 'POST':
        form = UploadResultsForm(request.POST, request.FILES)
        if form.is_valid():
            context['post_data'] = True
            month, day, year = request.POST['date_of_results'].split("/")
            result_date = datetime.date(year=int(year), month=int(month), day=int(day))
            results, errors = TestResult.results_from_xml_file(request.FILES['results_file'], product,
                                                               date=result_date, author=author)

            context['success'] = len(results)
            for result in results:
                result.save()

            if len(errors) > 0:
                context['errors'] = errors

            return render(request, "test_tracker/upload_results.html", context)
        else:
            context['errors'] = ['Invalid/missing form entries...']
    else:
        form = UploadResultsForm(
            initial={
                'author': author,
            }
        )

    context['form'] = form

    return render(request, "test_tracker/upload_results.html", context)
