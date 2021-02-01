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
from django.db import models, transaction
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_status import TestStatus
from test_tracker.models.test_case import TestCase
from test_tracker.models.test_result import TestResult


def dashboard(request, name, version):
    product = Product.objects.get(name=name, version=version)
    request_starting_date = request.GET.get('starting_date', None)
    requested_days = request.GET.get('requested_days', 5)

    try:
        if request_starting_date is not None:
            starting_date = models.DateField().to_python(request_starting_date)
        else:
            starting_date = datetime.date.today()
    except Exception:
        starting_date = datetime.date.today()

    table = [
        {
            'name': case.name,
            'category': case.category,
            'subcategory': case.subcategory,
            'results': TestResult.objects.filter(
                testcase=case,
                date__range=[starting_date - datetime.timedelta(days=int(requested_days)), starting_date]
            ),
        }
        for case in TestCase.objects.filter(product=product)
    ]

    context = {
        'product': product,
        'starting_date': starting_date,
        'requested_days': requested_days,
        'table': table,
    }

    return render(request, "test_tracker/dashboard.html", context)
