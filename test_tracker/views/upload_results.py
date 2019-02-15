"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from io import BytesIO
import base64
import datetime
import matplotlib.pyplot as plt

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.forms.upload_results_form import UploadResultsForm
from test_tracker.models.test_status import TestStatus


@login_required
def upload_results(request, name, version):

    context = {}

    product = Product.objects.get(name=name, version=version)
    author = request.user

    context['product'] = product
    context['author'] = author

    if request.method == 'POST':
        form = UploadResultsForm(request.POST, request.FILES)
        print('form recieved...')
    else:
        form = UploadResultsForm(
            initial={
                'author': author,
            }
        )

    context['form'] = form
    return render(request, "test_tracker/upload_results.html", context)
