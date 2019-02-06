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
    # General
    path('', views.dashboard_overview, name='index'),
    path('dashboard/<str:name>/<str:version>', views.dashboard, name='dashboard'),
    # Create
    path('create/product', views.ProductCreateView.as_view(), name='create_product'),
    path('create/testcase', views.TestCaseCreateView.as_view(), name='create_testcase'),
    path('create/result/<', views.TestResultCreateView.as_view(), name='create_result'),
    # Update
    path('update/product/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('update/testcase/<int:pk>', views.TestCaseUpdateView.as_view(), name='update_testcase'),
    path('update/result/<int:pk>', views.TestResultUpdateView.as_view(), name='update_result'),
]
