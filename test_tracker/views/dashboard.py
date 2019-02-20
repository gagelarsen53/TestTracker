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

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from test_tracker.models.product import Product


def dashboard(request, name, version):
    context = {
        'got_product': False,
        'test_cases': [],
        'product': None,
        'errors': []
    }

    # Get All products
    products = Product.objects.filter(active=True).order_by("name")
    context['products'] = products

    # Get the Product
    try:
        context['product'] = Product.objects.get(
            name=name,
            version=version
        )
        context['got_product'] = True
    except ObjectDoesNotExist:
        context['errors'].append("Could not find product...")

    # Get testcases
    testcases = []
    if context['product']:
        testcases = context['product'].get_test_cases()

    num_days = 5
    context['testcases'] = [
        {
            'testcase': testcase,
            'results': testcase.get_last_n_days_results(n_days=num_days, blanks=True)
        }
        for testcase in testcases
    ]

    today = datetime.date.today()
    context['dates'] = [today - datetime.timedelta(i) for i in range(num_days)]

    return render(request, "test_tracker/dashboard.html", context)


def dashboard_table(request, name, version):
    context = {
        'got_product': False,
        'test_cases': [],
        'product': None,
        'errors': []
    }

    # Get the Product
    try:
        context['product'] = Product.objects.get(
            name=name,
            version=version
        )
        context['got_product'] = True
    except ObjectDoesNotExist:
        context['errors'].append("Could not find product...")

    # Get testcases
    testcases = []
    if context['product']:
        testcases = context['product'].get_test_cases()

    num_days = 5
    context['testcases'] = [
        {
            'testcase': testcase,
            'results': testcase.get_last_n_days_results(n_days=num_days, blanks=True)
        }
        for testcase in testcases
        ]

    today = datetime.date.today()
    context['dates'] = [today - datetime.timedelta(i) for i in range(num_days)]

    return render(request, "test_tracker/dashboard_table.html", context)


