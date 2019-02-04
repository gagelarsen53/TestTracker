"""
********************************************************************************
* Name: urls.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('TestTracker/', include('test_tracker.urls')),
    path('admin/', admin.site.urls),
]
