"""
********************************************************************************
* Name: test_case.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime
import logging

from django.contrib.auth.models import User
from django.db import models

from test_tracker.models.product import Product
from test_tracker.models.test_category import TestCategory
from test_tracker.models.test_subcategory import TestSubcategory


log = logging.getLogger('test_tracker.' + __name__)


class TestCase(models.Model):
    """
    An object to represent a testcase
    """

    class Meta:
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"
        unique_together = ('product', 'name')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    source = models.CharField(max_length=64)
    summary = models.TextField()
    category = models.ForeignKey(TestCategory, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(TestSubcategory, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    needs_review = models.BooleanField(default=True)
    create_date = models.DateField(default=datetime.date.today)

    def get_last_n_days_results(self, n_days=30, blanks=False):
        from test_tracker.models.test_result import TestResult
        results = []

        # Get all results for test case
        today = datetime.date.today()
        last_date = today + datetime.timedelta(-1 * (n_days - 1))
        test_results = TestResult.objects.filter(
            testcase=self,
            date__range=[today, last_date],
        ).order_by('-date')

        if blanks:
            index = 0
            date_index = 0
            while date_index < n_days and index < len(test_results):
                if test_results[index].date == today + datetime.timedelta(-1 * date_index):
                    results.append(test_results[index])
                    index += 1
                else:
                    results.append(None)
                date_index += 1
        else:
            results = [x for x in test_results]

        return results

    def get_last_n_test_results(self, n=30):
        from test_tracker.models.test_result import TestResult

        # Get all results for test case
        test_results = TestResult.objects.filter(testcase=self).order_by('date')
        result_range = min(n, len(test_results))

        return [x for x in test_results[-1 * result_range]]

    def get_json(self):
        pass

    def get_xml(self):
        pass

    def __str__(self):
        pass
