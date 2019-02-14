"""
********************************************************************************
* Name: product.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import logging

from django.db import models

log = logging.getLogger('test_tracker.' + __name__)


class Product(models.Model):
    """
    A product
    """

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        unique_together = ('name', 'version')

    name = models.CharField(max_length=32)
    version = models.CharField(max_length=16)
    notes = models.TextField(max_length=256, blank=True, null=True)
    active = models.BooleanField(default=True)

    def get_test_cases(self, active_only=False):
        from test_tracker.models.test_case import TestCase

        # Get all testcases
        test_cases = TestCase.objects.filter(product=self).order_by('name')

        # Filter out in active
        if active_only:
            test_cases = test_cases.filter(active=True)

        return [x for x in test_cases]

    def get_results(self, days=30, blanks=True):
        results = {}
        test_cases = self.get_test_cases(active_only=True)
        for test_case in test_cases:
            results[test_case] = test_case.get_last_n_days_results(n_days=days, blanks=blanks)
        return results

    def get_results_for_date(self, result_date):
        from test_tracker.models.test_result import TestResult
        results = TestResult.objects.filter(
            testcase__product=self,
            date=result_date
        )
        return [x for x in results]

    def get_json(self):
        raise NotImplementedError("get_json function not yet implemented for product object")

    def get_xml(self):
        raise NotImplementedError("get_xml function not yet implemented for product object")

    def __str__(self):
        return "<Product: {}>".format(self.get_product_string())

    def get_product_string(self):
        return "{}-{}".format(self.name, self.version)

    def test_case_count(self):
        from test_tracker.models.test_case import TestCase
        return TestCase.objects.filter(product=self, active=True).count()
