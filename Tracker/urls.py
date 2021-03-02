"""
********************************************************************************
* Name: urls.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include

from Tracker.core_views import signup
from Tracker.core_views import landing

urlpatterns = [
    path("", landing.landing, name='landing'),
    path('TestTracker/', include('test_tracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/logout/', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/password_change/', include('django.contrib.auth.urls'), name='password_change'),
    path('accounts/password_change_done/', include('django.contrib.auth.urls'), name='password_change_done'),
    path('accounts/password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    path('accounts/password_reset_done', include('django.contrib.auth.urls'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    path('accounts/reset/done', include('django.contrib.auth.urls'), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('signup/', signup.signup, name='signup'),
]
