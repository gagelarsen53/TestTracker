"""
********************************************************************************
* Name: test_subcategory.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import logging

from django.db import models

from test_tracker.models.test_category import TestCategory


log = logging.getLogger('test_tracker.' + __name__)


class TestSubcategory(models.Model):
    """
    A sub category field for each type of test type

    category (ForeignKey): a category model object
    subcategory (CharField): a string to represent the subcategory
    description (CharField): a string to describe the subcategory
    """

    class Meta:
        verbose_name = "Test Subcategory"
        unique_together = ('category', 'subcategory')

    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=32)
    description = models.CharField(max_length=64, default="No description provided...")

    def get_json(self):
        return {"subcategory": self.subcategory}

    def get_xml(self):
        return "<TestSubcategory>{}</TestSubcategory>".format(self.subcategory)

    def __str__(self):
        return "<TestSubcategory: {}>".format(self.subcategory)
