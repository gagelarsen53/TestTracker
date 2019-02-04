from django.test import TestCase
from test_tracker.models.test_category import TestCategory


class TestCategoryTest(TestCase):
    def setUp(self):
        self.category_1 = TestCategory(
            category="Category1",
            description="basic category description",
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
        category_1 = self.category_1.get_json()
        self.assertEqual({"category": "Category1"}, category_1)

        category_2 = self.category_2.get_json()
        self.assertEqual({"category": "Category2"}, category_2)

    def test_get_xml(self):
        category_1 = self.category_1.get_xml()
        self.assertEqual("<TestCategory>Category1</TestCategory>", category_1)

        category_2 = self.category_2.get_xml()
        self.assertEqual("<TestCategory>Category2</TestCategory>", category_2)

    def test_str(self):
        category_1 = str(self.category_1)
        self.assertEqual("<TestCategory: Category1>", category_1)

        category_2 = str(self.category_2)
        self.assertEqual("<TestCategory: Category2>", category_2)

    def test_description(self):
        description = self.category_1.description
        self.assertEqual("basic category description", description)

    def test_description_default(self):
        description = self.category_2.description
        self.assertEqual("No description provided...", description)
