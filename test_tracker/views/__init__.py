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
from test_tracker.views.daily_stats import daily_stats
from test_tracker.views.upload_results import upload_results
from test_tracker.views.upload_testcases import upload_testcases
from test_tracker.views.form_views import ProductCreateView
from test_tracker.views.form_views import ProductUpdateView
from test_tracker.views.form_views import TestCaseCreateView
from test_tracker.views.form_views import TestCaseUpdateView
from test_tracker.views.form_views import TestResultCreateView
from test_tracker.views.form_views import TestResultUpdateView
from test_tracker.views.form_views import TestCategoryCreateView
from test_tracker.views.form_views import TestSubcategoryCreateView
from test_tracker.views.form_views import TestStatusCreateView


