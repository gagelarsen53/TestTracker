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


def daily_stats(request, name, version, day, month, year):
    context = {
        'got_product': False,
        'test_cases': [],
        'product': None,
    }

    return render(request, "test_tracker/daily_stats.html", context)
