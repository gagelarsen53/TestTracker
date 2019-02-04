from django.test import TestCase
from test_tracker.models.test_category import TestCategory


class TestCategoryTest(TestCase):
    def setUp(self):
        self.category_1 = TestCategory(
            category="Category1",
            description="basic test description",
        )
        self.category_1.save()

        self.category_2 = TestCategory(
            category="Category2",
        )
        self.category_2.save()

    def tearDown(self):
        self.category_1.delete()
        self.category_2.delete()

    def test_get_json(self):
        sp_json = self.category_1.get_json()
        self.assertEqual({"category": "Category1"}, sp_json)

        sf_json = self.category_2.get_json()
        self.assertEqual({"category": "Category2"}, sf_json)

    def test_get_xml(self):
        sp_xml = self.category_1.get_xml()
        self.assertEqual("<TestCategory>Category1</TestCategory>", sp_xml)

        sf_xml = self.category_2.get_xml()
        self.assertEqual("<TestCategory>Category2</TestCategory>", sf_xml)

    def test_str(self):
        sp_str = str(self.category_1)
        self.assertEqual("<TestCategory: Category1>", sp_str)

        sf_str = str(self.category_2)
        self.assertEqual("<TestCategory: Category2>", sf_str)

    def test_description(self):
        description = self.category_1.description
        self.assertEqual("basic test description", description)

    def test_description_default(self):
        description = self.category_2.description
        self.assertEqual("No description provided...", description)
