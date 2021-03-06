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
from test_tracker.models.test_result import TestResult


def dashboard_overview(request):
    context = {}

    # Get All products
    products = Product.objects.filter(active=True).order_by("name")
    context['products'] = products
    return render(request, "test_tracker/dashboard_overview.html", context)




# product = Product.objects.get(name="GMS", version="Dev")
#
# context = {
#     'product': product
# }
#
# results = product.get_results(days=45, blanks=False)
#
# # successes, errors = TestCase.test_cases_from_json_file('C:\\Personal\\TestTracker\\test_tracker\\models\\test.json')
# # for success in successes:
# #     success.save()
#
# # successes, errors = TestResult.results_from_xml_file('C:\\Personal\\TestTracker\\test_tracker\\models\\results.xml',
# #                                                      product=product, author=request.user)
# # for success in successes:
# #     success.save()
#
# context['results'] = results
# context['errors'] = errors
# context['successes'] = successes