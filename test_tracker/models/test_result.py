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
import re
import xml.etree.ElementTree as ET

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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

    def get_json(self):
        pass

    def get_xml(self):
        pass

    def __str__(self):
        return "<TestResult: {} - {}>".format(self.testcase.name, self.date)

    @classmethod
    def results_from_xml_file(cls, _xml_file, product, author, date):
        errors = []
        successes = []
        results = {
            '0': TestStatus.objects.get(status='Pass'),
            '1': TestStatus.objects.get(status='Pass'),
            '2': TestStatus.objects.get(status='Fail'),
        }

        # Read the XML File
        tree = None
        try:
            tree = ET.parse(_xml_file)
        except ET.ParseError:
            errors.append("Unable to parse provided xml file")
            return successes, errors

        root = tree.getroot()
        nodes = root.findall('./Node/Node')
        print(len(nodes))
        tests = {}
        for node in nodes:
            prps = node.findall('./Prp')
            name = None
            status = None
            for prp in prps:
                p_name = prp.attrib.get("name", None)
                p_value = prp.attrib.get("value", None)
                if p_name == "name" and ("[Script\\" in str(p_value) or str(p_value).startswith('Script Test Log')):
                    name = p_value
                if p_name == "status":
                    status = p_value
            if not name or not status:
                continue

            test_name_re = r'.*?\[Script\\.*? - (?:[Tt]est_)?([A-Za-z0-9_]*)\]'
            test_name_re_old = r'Script Test Log \[[A-Za-z_]*\\(?:[Tt]est_)?([A-Za-z0-9_]*)\]'
            test_name_search = re.search(test_name_re, name)
            if not test_name_search:
                test_name_search = re.search(test_name_re_old, name)
            if not test_name_search:
                errors.append("Test is not named properly: '{}'".format(name))
                continue

            test_name = test_name_search.group(1)

            if test_name in tests.keys():
                errors.append("result for '{}' defined twice in specifed xml file.".format(test_name))
                continue

            tests[test_name] = results[status]

        for test in tests.keys():
            if date == None:
                test_date = datetime.date.today()
            else:
                test_date = date
            test_case = None
            try:
                test_case = TestCase.objects.get(product=product, name=test)
            except ObjectDoesNotExist:
                errors.append("Test Case '{}' for '{}' does not exist".format(test, product))
                continue

            # Make sure it is not a duplicate
            if cls.objects.filter(testcase=test_case, date=test_date).count() > 0:
                errors.append("test_result for '{}' already exists for specifed date {}".format(test_case, test_date))
                continue

            note = "uploaded result..."
            tr = cls(
                date=test_date,
                status=tests[test],
                author=author,
                testcase=test_case,
                note=note
            )
            successes.append(tr)

        return successes, errors

