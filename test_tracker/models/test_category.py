"""
********************************************************************************
* Name: test_category.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import logging

from django.db import models


log = logging.getLogger('test_tracker.' + __name__)


class TestCategory(models.Model):
    """
    A category field for each type of test type

    category (CharField): a string to represent the category
    description (CharField): a string to describe the category
    """

    class Meta:
        verbose_name = "Test Category"

    category = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=64, default="No description provided...")

    def get_json(self):
        return {"category": self.category}

    def get_xml(self):
        return "<TestCategory>{}</TestCategory>".format(self.category)

    def __str__(self):
        return "<TestCategory: {}>".format(self.category)
