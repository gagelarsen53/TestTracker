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
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_status import TestStatus
from test_tracker.models.test_case import TestCase
from test_tracker.models.test_result import TestResult


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
    request_days = request.GET.get("days", 5)
    try:
        num_days = int(request_days)
    except:
        num_days = 5

    request_show_blanks = request.GET.get("show_empty_days", False)
    tcs = context['product'].get_last_n_days_results(n_days=num_days, blanks=request_show_blanks)

    context['testcases'] = tcs
    context['dates'] = [result[1] for result in context['testcases'][0]['results']]

    return render(request, "test_tracker/dashboard_table.html", context)


def dashboard_info(request, name, version):
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
    testcases_and_results = [
        {
            'testcase': testcase,
            'results': testcase.get_last_n_days_results(n_days=num_days, blanks=True)
        }
        for testcase in testcases
        ]

    status_objects = TestStatus.objects.all().values('status')
    statuses = [{x['status']: [z['results'][y][1] for z in testcases_and_results if z['results'][y][0] is not None and x['status'] == z['results'][y][0].status.status and z['testcase'].active]
                 for x in status_objects} for y in range(0, num_days)]

    # Calculate Information
    total_test_cases = len(testcases)
    active_test_cases = [x for x in testcases if x.active]
    total_active_test_cases = len(active_test_cases)

    found_results = False
    index = 0
    while not found_results and index < num_days:
        passing_test_case_count = len(statuses[index]['Pass'])
        failing_test_case_count = len(statuses[index]['Fail'])
        issue_test_case_count = len(statuses[index]['Issue'])
        bug_test_case_count = len(statuses[index]['Bug'])
        under_construction_test_case_count = len(statuses[index]['Under Construction'])
        no_result_test_case_count = total_active_test_cases - (passing_test_case_count + failing_test_case_count + \
                                                               issue_test_case_count + bug_test_case_count + \
                                                               under_construction_test_case_count)

        if passing_test_case_count > 0 or \
              failing_test_case_count > 0 or \
              issue_test_case_count > 0 or \
              bug_test_case_count > 0 or \
              under_construction_test_case_count > 0:
            found_results = True
            context['recent_result_date'] = datetime.date.today() - datetime.timedelta(days=index)

        index += 1

    context['total_test_case_count'] = total_test_cases
    context['active_test_case_count'] = total_active_test_cases
    context['passing_test_case_count'] = passing_test_case_count
    context['failing_test_case_count'] = failing_test_case_count
    context['issue_test_case_count'] = issue_test_case_count
    context['bug_test_case_count'] = bug_test_case_count
    context['under_construction_test_case_count'] = under_construction_test_case_count
    context['no_result_test_case_count'] = no_result_test_case_count

    return render(request, "test_tracker/dashboard_info.html", context)


@login_required
@transaction.atomic
def delete_results_for_date(request, name, version, day, month, year):
    product = Product.objects.get(name=name, version=version)
    date = datetime.datetime(year=year, day=day, month=month)
    TestResult.objects.filter(testcase__product=product, date=date).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@transaction.atomic
def copy_result_to_current_date(request, name, version, day, month, year, pk):
    product = Product.objects.get(name=name, version=version)
    date = datetime.datetime(year=year, day=day, month=month)
    result_dates = TestResult.objects.filter(testcase__product=product).values('date').distinct()
    current_result_date = max([date['date'] for date in result_dates])
    copied_result = TestResult.objects.get(testcase__product=product, pk=pk, date=date)
    testcase = copied_result.testcase
    note = copied_result.note + " (COPIED)"

    try:
        cur_result = TestResult.objects.get(testcase__product=product, testcase=testcase, date=current_result_date)
        cur_result.status = copied_result.status
        cur_result.note = note
        cur_result.author = request.user
        cur_result.save()
    except ObjectDoesNotExist:
        new_result = TestResult(
            date=current_result_date,
            status=copied_result.status,
            author=request.user,
            testcase=testcase,
            note=note,
        )
        new_result.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
