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


def dashboard_overview(request):
    product = Product.objects.get(name="GMS", version="Dev")

    context = {
        'product': product
    }

    results = product.get_results(days=45, blanks=True)

    context['results'] = results

    return render(request, "test_tracker/dashboard_overview.html", context)
