"""
********************************************************************************
* Name: test_result.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime
import logging

from django.contrib.auth.models import User
from django.db import models

from test_tracker.models.test_case import TestCase
from test_tracker.models.test_status import TestStatus


log = logging.getLogger('test_tracker.' + __name__)


class TestResult(models.Model):
    """
    A testresult
    """

    class Meta:
        verbose_name = "Test Result"
        verbose_name_plural = "Test Results"

    date = models.DateField(default=datetime.date.today)
    status = models.ForeignKey(TestStatus, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    note = models.TextField(max_length=256)

