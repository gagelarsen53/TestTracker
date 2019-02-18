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
    # Statistics
    path('dashboard/<str:name>/<str:version>/<int:day>-<int:month>-<int:year>',
         views.daily_stats, name='daily_stats'),
    # Dashboard
    path('dashboard/<str:name>/<str:version>', views.dashboard, name='dashboard'),
    # Upload
    path('upload/results/<str:name>/<str:version>', views.upload_results, name='upload_results'),
    # Create
    path('create/product', views.ProductCreateView.as_view(), name='create_product'),
    path('create/testcase', views.TestCaseCreateView.as_view(), name='create_testcase'),
    path('create/result', views.TestResultCreateView.as_view(), name='create_result'),
    path('create/testcategory', views.TestCategoryCreateView.as_view(), name='create_testcategory'),
    path('create/testsubcategory', views.TestSubcategoryCreateView.as_view(), name='create_testsubcategory'),
    path('create/teststatus', views.TestStatusCreateView.as_view(), name='create_teststatus'),
    # Update
    path('update/product/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
    path('update/testcase/<int:pk>', views.TestCaseUpdateView.as_view(), name='update_testcase'),
    path('update/result/<int:pk>', views.TestResultUpdateView.as_view(), name='update_result'),
]
