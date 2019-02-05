"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_case import TestCase


def dashboard_overview(request):
    product = Product.objects.get(name="GMS", version="Dev")

    context = {
        'product': product
    }

    results = product.get_results(days=45, blanks=False)

    successes, errors = TestCase.test_cases_from_json_file('C:\\Personal\\TestTracker\\test_tracker\\models\\test.json')
    for success in successes:
        success.save()

    context['results'] = results
    context['errors'] = errors
    context['successes'] = successes

    return render(request, "test_tracker/dashboard_overview.html", context)
