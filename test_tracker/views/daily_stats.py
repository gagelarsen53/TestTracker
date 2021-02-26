"""
********************************************************************************
* Name: dashboard_stats.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime
import json

from django.shortcuts import render

from test_tracker.models.product import Product
from test_tracker.models.test_status import TestStatus


def daily_stats(request, name, version, day, month, year):
    context = {}

    products = Product.objects.filter(active=True).order_by("name")
    context['products'] = products
    result_date = datetime.date(month=month, day=day, year=year)
    context['date'] = result_date
    product = Product.objects.get(name=name, version=version)
    context['product'] = product

    # Get Stats for Pie Chart
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
            issues.append((result.testcase.name, get_cleaned_note(result)))
        if result.status.status == "Bug":
            bugs.append((result.testcase.name, get_cleaned_note(result)))
    context['issue_notes'] = issues
    context['bug_notes'] = bugs
    context['counts'] = {x: len(test_status[x]) for x in test_status.keys()}

    # Pie Chart
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

    # Stats for Line Chart
    num_days = 14
    date_status_counts = {}
    desired_statuses = ['Pass', 'Fail', 'False Negative', 'Issue', 'Bug']
    test_cases = [tc for tc in product.get_test_cases()]
    results_over_time = [testcase.get_last_n_days_results(n_days=num_days + 1) for testcase in test_cases]
    for testcase in results_over_time:
        for day_with_result in testcase:
            date = day_with_result[0].date
            if date not in date_status_counts.keys():
                date_status_counts[date] = {}
                for desired_status in desired_statuses:
                    date_status_counts[date][desired_status] = 0
            status = day_with_result[0].status.status
            if status in date_status_counts[date].keys():
                date_status_counts[date][status] += 1

    status_counts_over_time = {}
    for status in desired_statuses:
        status_counts_over_time[status] = []

    dates = sorted(list(date_status_counts.keys()))
    dates.reverse()
    for date in dates:
        for status in date_status_counts[date]:
            status_counts_over_time[status].append(date_status_counts[date][status])

    line_chart_datasets = []
    for status in status_counts_over_time:
        line_chart_datasets.append({
            'label': status,
            'borderColor': available_statuses[status].hex_color,
            'data': status_counts_over_time[status],
            'fill': False,
            'lineTension': 0,
            'pointBorderWidth': 5,
            'pointHitRadius': 1000
        })

    dates = [d.strftime('%b %d') for d in sorted(list(date_status_counts.keys()))]
    dates.reverse()

    context['line_chart_data'] = {
        'labels': dates,
        'datasets': json.dumps(line_chart_datasets),
        'today_date': datetime.datetime.today().strftime('%b %d'),
        'two_weeks_date': (datetime.datetime.today() - datetime.timedelta(days=num_days)).strftime('%b %d')
    }

    return render(request, "test_tracker/daily_stats.html", context)


def get_cleaned_note(result):
    note = result.note
    note = note.replace(' (COPIED)', '')
    return note
