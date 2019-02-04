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


log = logging.getLogger('test_tracker.' + __name__)


class TestSubcategory(models.Model):
    """
    A sub category field for each type of test type

    subcategory (CharField): a string to represent the subcategory
    description (CharField): a string to describe the subcategory
    """

    class Meta:
        verbose_name = "Test Subcategory"
        verbose_name_plural = "Test Subcategories"

    subcategory = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=64, default="No description provided...")

    def get_json(self):
        return {"subcategory": self.subcategory}

    def get_xml(self):
        return "<TestSubcategory>{}</TestSubcategory>".format(self.subcategory)

    def __str__(self):
        return "<TestSubcategory: {}>".format(self.subcategory)
