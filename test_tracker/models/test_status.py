"""
********************************************************************************
* Name: test_status.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import logging

from django.db import models


log = logging.getLogger('test_tracker.' + __name__)


class TestStatus(models.Model):
    """
    A status field for each type of test result

    status (CharField): a string to represent the status
    hex_color (CharField): a string to represent the color of the status
    """

    class Meta:
        verbose_name = "Test Status"
        verbose_name_plural = "Test Status"

    status = models.CharField(max_length=32, unique=True)
    hex_color = models.CharField(max_length=12, default="#ffffff")
    text_hex_color = models.CharField(max_length=12, default="#000000")

    def get_json(self):
        return {"status": self.status}

    def get_xml(self):
        return "<TestStatus>{}</TestStatus>".format(self.status)

    def __str__(self):
        return "{}".format(self.status)
