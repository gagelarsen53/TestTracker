"""
********************************************************************************
* Name: needs_review.py
* Author: Matt LeBaron
* Created On: February 9, 2021
* Copyright: (c) GLD
********************************************************************************
"""
from django.shortcuts import render

from test_tracker.models.product import Product


def needs_review(request, name, version):
    context = {}

    products = Product.objects.filter(active=True).order_by("name")
    context['products'] = products

    product = Product.objects.get(name=name, version=version)
    context['product'] = product

    all_testcases = product.get_test_cases()
    testcases = [testcase for testcase in all_testcases if testcase.needs_review]
    context['testcases'] = testcases

    return render(request, "test_tracker/needs_review.html", context)
