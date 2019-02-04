"""
********************************************************************************
* Name: dashboard_overview.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.shortcuts import render


def dashboard_overview(request):
    context = {}
    return render(request, "test_tracker/dashboard_overview.html", context)
