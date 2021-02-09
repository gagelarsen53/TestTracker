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

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_status import TestStatus
from test_tracker.models.test_case import TestCase
from test_tracker.models.test_result import TestResult


def dashboard2(request, name, version):
    context = {}

    product = Product.objects.get(name=name, version=version)

    context['product'] = product

    testcases = TestCase.objects.filter(product=product)
    testcases_list = []

    for testcase in testcases:
        testcase_dict = {
            'id': testcase.id,
            'name': testcase.name,
            'last_status_class': 'none',
            'last_status': 'None',
            'category': testcase.category.category,
            'subcategory': testcase.subcategory.subcategory,
            'out_of_date_class': 'last-result-very-out-of-date',
            'days_since_last': '-',
            'active_status': 'Active'
        }

        case_result = TestResult.objects.filter(testcase=testcase).order_by('date')
        if len(case_result) > 0:
            last_result = case_result[0]
            days_since = (datetime.date.today() - last_result.date).days
            testcase_dict.update({
                'last_status_class': last_result.status.status.lower().replace(' ', '-'),
                'last_status': last_result.status.status,
                'days_since_last': days_since,
                'out_of_date_class': None if days_since < 3 else 'last-result-out-of-date' if days_since < 7 else 'last-result-very-out-of-date'
            })
        testcases_list.append(testcase_dict)

    context['testcases'] = testcases_list

    return render(request, "test_tracker/dashboard2.html", context)
