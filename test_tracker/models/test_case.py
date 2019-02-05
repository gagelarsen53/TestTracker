"""
********************************************************************************
* Name: test_case.py
* Author: Gage Larsen
* Created On: February 4, 2019
* Copyright: (c) GLD
********************************************************************************
"""
import datetime
import json
import logging

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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
            date__range=[last_date, today],
        ).order_by('-date')

        if blanks:
            index = 0
            date_index = 0
            while date_index < n_days:
                date_delta = today + datetime.timedelta(-1 * date_index)
                if index < len(test_results) and test_results[index].date == date_delta:
                    results.append((test_results[index], date_delta))
                    index += 1
                else:
                    results.append((None, date_delta))
                date_index += 1
        else:
            results = [(x, x.date) for x in test_results]
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
        return "<TestCase: {}>".format(self.name)

    @classmethod
    def test_cases_from_json_file(cls, _json_file):
        errors = []
        successes = []
        json_required = ['product', 'version', 'test_cases']
        required_fields = ['name', 'author', 'source']
        defaults = {
            'summary': 'no summary provided...',
            'category': 'Undefined',
            'subcategory': 'Undefined',
            'active': True,
            'needs_review': True,
            'create_date': datetime.date.today(),
        }

        # Get the json data
        data = {}
        try:
            with open(_json_file, 'r') as jf:
                data = json.load(jf)
        except IOError:
            errors.append("Could not read file: {}".format(_json_file))
        except ValueError:
            errors.append("Could not decode json file: {}".format(_json_file))

        # exit if there are any errors
        if len(errors) > 0:
            return successes, errors

        # Ensure read json has correct keys
        if not set(json_required).issubset(set(data.keys())):
            missing_keys = [x for x in json_required if x not in data.keys()]
            errors.append("missing required keys in json: {}".format(",".join(missing_keys)))
            return successes, errors

        # Make sure specified product exists
        try:
            product = Product.objects.get(
                name=data['product'],
                version=data['version'],
            )
        except ObjectDoesNotExist:
            errors.append("specified product does not exist: {} {}".format(data['product'], data['version']))
            return successes, errors

        # Loop through the test cases and create dictionary
        test_cases = [
            {
                'product': product,
                'name': tc.get('name', None),
                'author': tc.get('author', None),
                'source': tc.get('source', None),
                'summary': tc.get('summary', defaults['summary']),
                'category': tc.get('category', defaults['category']),
                'subcategory': tc.get('subcategory', defaults['subcategory']),
                'active': tc.get('active', defaults['active']),
                'needs_review': tc.get('needs_review', defaults['needs_review']),
            }
            for tc in data['test_cases']
            ]

        # Check for at least 1 test case
        if not len(test_cases) > 0:
            errors.append("No Test Cases defined in specified json file: {}".format(_json_file))
            return successes, errors

        # Create test cases if possible
        new_created_test_names = []
        for test_case in test_cases:
            # Check required fields
            if None in [test_case[x] for x in required_fields]:
                errors.append("invalid test_case: {}".format(test_case))
                continue

            # Get category and subcategory
            try:
                category = TestCategory.objects.get(category=test_case['category'])
                subcategory = TestSubcategory.objects.get(subcategory=test_case['subcategory'])
            except ObjectDoesNotExist:
                errors.append("invalid category/subcategory specifed for '{}': {}/{}".format(
                    test_case['name'], test_case['category'], test_case['subcategory']
                ))
                continue

            # Make sure it is not a duplicate
            if cls.objects.filter(product=test_case['product'], name=test_case['name']).count() > 0:
                errors.append("test_case with name '{}' for product '{}' already exists".format(
                    test_case['name'], test_case['product']
                ))
                continue
            if test_case['name'] in new_created_test_names:
                errors.append("test_case with name '{}' defined multiple times in this json file".format(
                    test_case['name']
                ))
                continue

            # Make sure user exists
            user = None
            try:
                user = User.objects.get(username=test_case['author'])
            except ObjectDoesNotExist:
                errors.append("author '{}' specified for '{}' does not exist in the TestTracker database".format(
                    test_case['author'], test_case['name']
                ))

            # Create Object
            try:
                tc = cls(
                    product=test_case['product'],
                    name=test_case['name'],
                    author=user,
                    source=test_case['source'],
                    summary=test_case['summary'],
                    category=category,
                    subcategory=subcategory,
                    active=bool(test_case['active']),
                    needs_review=bool(test_case['needs_review']),
                )
                successes.append(tc)
                new_created_test_names.append(test_case['name'])
            except Exception as e:
                errors.append("Problem encountered while creating {} for {}: {}".format(
                    test_case['name'], test_case['product'], e
                ))

        return successes, errors
