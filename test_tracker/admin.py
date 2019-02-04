"""
********************************************************************************
* Name: admin.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
from django.contrib import admin
from test_tracker.models.test_status import TestStatus
from test_tracker.models.test_category import TestCategory
from test_tracker.models.test_subcategory import TestSubcategory


@admin.register(TestStatus)
class TestStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'description')


@admin.register(TestSubcategory)
class TestSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'description')
