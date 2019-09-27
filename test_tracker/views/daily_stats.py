"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from io import BytesIO
import numpy as np
import base64
import datetime
import matplotlib.pyplot as plt

from django.core.exceptions import ObjectDoesNotExist
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

    # Status Graph
    available_statuses = {ts.status: ts for ts in TestStatus.objects.filter()}
    test_status = {}
    for ts in available_statuses.values():
        test_status[ts.status] = []
    for result in results:
        test_status[result.status.status].append(result)
    test_status['Inactive'] = [None for x in test_cases if not x.active]
    active_test_cases = [tc for tc in test_cases if tc.active]
    test_status['No Results'] = [None for x in range(0, len(active_test_cases) - len(results))]

    labels = [x for x in test_status.keys() if len(test_status[x]) > 0]
    sizes = [len(test_status[x]) for x in labels]
    colors = [x.hex_color for x in available_statuses.values() if x.status in labels]
    colors.append("#a89a9a")  # Inactive
    colors.append("#d3a0a0")  # No Results
    fig1, ax1 = plt.subplots()
    total = sum(sizes)/100.0
    autopct = lambda x: "%d" % round(x*total)

    plt.xticks(np.arange(len(labels)), labels)
    b = ax1.bar(np.arange(len(labels)), sizes, align='center', alpha=0.5, color=colors)
    # plt.legend([b], labels)

    # ax1.pie(sizes, labels=labels, shadow=False, startangle=90, colors=colors, autopct=autopct)
    # ax1.axis('equal')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic_1 = base64.b64encode(image_png)
    context['test_status'] = graphic_1.decode('utf-8')

    context['counts'] = {x: len(test_status[x]) for x in test_status.keys()}

    return render(request, "test_tracker/daily_stats.html", context)
