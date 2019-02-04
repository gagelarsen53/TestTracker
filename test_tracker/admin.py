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
from test_tracker.models.product import Product
from test_tracker.models.test_case import TestCase
from test_tracker.models.test_result import TestResult


@admin.register(TestStatus)
class TestStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'description')


@admin.register(TestSubcategory)
class TestSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('active', 'name', 'version')
    list_filter = ('name', 'active')


class TestResultInline(admin.TabularInline):
    model = TestResult
    max_num = 10
    extra = 0


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'create_date', 'author', 'active')
    list_filter = ('product', 'active', 'author', 'category', 'needs_review', 'create_date')
    inlines = [TestResultInline]
