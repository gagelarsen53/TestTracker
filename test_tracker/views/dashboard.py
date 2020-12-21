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
    context = {}
    return render(request, "test_tracker/dashboard.html", context)
