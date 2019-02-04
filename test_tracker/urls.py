"""
********************************************************************************
* Name: urls.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.urls import path

from test_tracker import views

urlpatterns = [
    path('', views.dashboard_overview, name='dashboard_overview'),
]
