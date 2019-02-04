from django.test import TestCase
from test_tracker.models.test_category import TestCategory
from test_tracker.models.test_subcategory import TestSubcategory


class TestSubcategoryTest(TestCase):
    def setUp(self):
        self.subcategory_1 = TestSubcategory(
            subcategory="Subcategory1",
            description="basic subcategory description",
        )
        self.subcategory_1.save()

        self.subcategory_2 = TestSubcategory(
            subcategory="Subcategory2",
        )
        self.subcategory_2.save()

    def tearDown(self):
        self.subcategory_1.delete()
        self.subcategory_2.delete()

    def test_get_json(self):
        subcategory_1 = self.subcategory_1.get_json()
        self.assertEqual({"subcategory": "Subcategory1"}, subcategory_1)

        subcategory_2 = self.subcategory_2.get_json()
        self.assertEqual({"subcategory": "Subcategory2"}, subcategory_2)

    def test_get_xml(self):
        subcategory_1 = self.subcategory_1.get_xml()
        self.assertEqual("<TestSubcategory>Subcategory1</TestSubcategory>", subcategory_1)

        subcategory_2 = self.subcategory_2.get_xml()
        self.assertEqual("<TestSubcategory>Subcategory2</TestSubcategory>", subcategory_2)

    def test_str(self):
        subcategory_1 = str(self.subcategory_1)
        self.assertEqual("<TestSubcategory: Subcategory1>", subcategory_1)

        subcategory_2 = str(self.subcategory_2)
        self.assertEqual("<TestSubcategory: Subcategory2>", subcategory_2)

    def test_description(self):
        description = self.subcategory_1.description
        self.assertEqual("basic subcategory description", description)

    def test_description_default(self):
        description = self.subcategory_2.description
        self.assertEqual("No description provided...", description)
