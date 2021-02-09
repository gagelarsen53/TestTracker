"""
********************************************************************************
* Name: __init__.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from test_tracker.views.dashboard_overview import dashboard_overview
from test_tracker.views.dashboard import dashboard
from test_tracker.views.dashboard import dashboard_table
from test_tracker.views.dashboard import dashboard_info
from test_tracker.views.dashboard import delete_results_for_date
from test_tracker.views.dashboard import copy_result_to_current_date
from test_tracker.views.daily_stats import daily_stats
from test_tracker.views.needs_review import needs_review
from test_tracker.views.upload_results import upload_results
from test_tracker.views.upload_testcases import upload_testcases
from test_tracker.views.form_views import ProductCreateView
from test_tracker.views.form_views import ProductUpdateView
from test_tracker.views.form_views import ProductDeleteView
from test_tracker.views.form_views import ProductDuplicateView
from test_tracker.views.form_views import TestCaseCreateView
from test_tracker.views.form_views import TestCaseUpdateView
from test_tracker.views.form_views import TestCaseDeleteView
from test_tracker.views.form_views import TestResultCreateView
from test_tracker.views.form_views import TestResultUpdateView
from test_tracker.views.form_views import TestResultDeleteView
from test_tracker.views.form_views import TestCategoryCreateView
from test_tracker.views.form_views import TestSubcategoryCreateView
from test_tracker.views.form_views import TestStatusCreateView
from test_tracker.views.async_views import async_update_case
from test_tracker.views.async_views import async_update_results
