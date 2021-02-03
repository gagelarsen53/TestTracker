"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime

from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_status import TestStatus


def daily_stats(request, name, version, day, month, year):
    context = {}

    result_date = datetime.date(month=month, day=day, year=year)
    context['date'] = result_date
    product = Product.objects.get(name=name, version=version)
    context['product'] = product

    # Get Stats
    test_cases = [tc for tc in product.get_test_cases() if tc.create_date <= result_date]
    results = product.get_results_for_date(result_date=result_date)
    available_statuses = {ts.status: ts for ts in TestStatus.objects.all()}
    test_status = {}
    issues = []
    bugs = []
    for ts in available_statuses.values():
        test_status[ts.status] = []
    for result in results:
        test_status[result.status.status].append(result)
        if result.status.status == "Issue":
            issues.append(result)
        if result.status.status == "Bug":
            bugs.append(result)
    context['issues'] = issues
    context['bugs'] = bugs
    test_status['Inactive'] = [None for x in test_cases if not x.active]
    active_test_cases = [tc for tc in test_cases if tc.active]
    test_status['No Results'] = [None for x in range(len(active_test_cases) - len(results))]
    context['counts'] = {x: len(test_status[x]) for x in test_status.keys()}

    # Graph
    labels = []
    counts = []
    colors = []
    for label in context['counts']:
        labels.append(label)
        counts.append(context['counts'][label])
        if label == 'Inactive':
            colors.append('#a89a9a')
        elif label == 'No Results':
            colors.append('#d3a0a0')
        else:
            colors.append(available_statuses[label].hex_color)
    context['piechart'] = {
        'labels': labels,
        'counts': counts,
        'colors': colors
    }

    return render(request, "test_tracker/daily_stats.html", context)
