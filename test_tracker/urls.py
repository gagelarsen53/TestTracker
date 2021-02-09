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
    # Delete All For Date
    path('dashboard/<str:name>/<str:version>/<int:day>-<int:month>-<int:year>/delete',
         views.delete_results_for_date, name='delete_results_for_date'),
    path('dashboard/<str:name>/<str:version>/<int:day>-<int:month>-<int:year>/copy/<int:pk>',
         views.copy_result_to_current_date, name='copy_result_to_current_date'),
    # Dashboard
    path('dashboard/<str:name>/<str:version>', views.dashboard, name='dashboard'),
    path('dashboard/<str:name>/<str:version>/table', views.dashboard_table, name='dashboard_table'),
    path('dashboard/<str:name>/<str:version>/info', views.dashboard_info, name='dashboard_info'),
    # Dashboard 2
    path('dashboard2/<str:name>/<str:version>', views.dashboard2, name='dashboard2'),
    # Upload
    path('upload/results/<str:name>/<str:version>', views.upload_results, name='upload_results'),
    path('upload/testcases/<str:name>/<str:version>', views.upload_testcases, name='upload_testcases'),
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
    # Delete
    path('delete/product/<int:pk>', views.ProductDeleteView.as_view(), name='delete_product'),
    path('delete/testcase/<int:pk>', views.TestCaseDeleteView.as_view(), name='delete_testcase'),
    path('delete/result/<int:pk>', views.TestResultDeleteView.as_view(), name='delete_testresult'),
    # Duplicate
    path('duplicate/product/<int:pk>', views.ProductDuplicateView.as_view(), name='duplicate_product'),
    # Async
    path('async/update/result/<int:pk>', views.async_update_results, name='async_update_results')
]
