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
    path('', views.dashboard_overview, name='index'),
    path('create/product', views.ProductCreateView.as_view(), name='create_product'),
    path('update/product/<int:pk>', views.ProductUpdateView.as_view(), name='update_product'),
]
