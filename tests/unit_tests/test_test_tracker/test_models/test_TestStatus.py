from django.test import TestCase
from test_tracker.models.test_status import TestStatus


class TestStatusTest(TestCase):
    def setUp(self):
        self.status_pass = TestStatus(
            status="Pass",
            hex_color="",
        )
        self.status_pass.save()

        self.status_fail = TestStatus(
            status="Fail",
        )
        self.status_fail.save()

    def tearDown(self):
        self.status_pass.delete()
        self.status_fail.delete()

    def test_get_json(self):
        sp_json = self.status_pass.get_json()
        self.assertEqual({"status": "Pass"}, sp_json)

        sf_json = self.status_fail.get_json()
        self.assertEqual({"status": "Fail"}, sf_json)

    def test_get_xml(self):
        sp_xml = self.status_pass.get_xml()
        self.assertEqual("<TestStatus>Pass</TestStatus>", sp_xml)

        sf_xml = self.status_fail.get_xml()
        self.assertEqual("<TestStatus>Fail</TestStatus>", sf_xml)

    def test_str(self):
        sp_str = str(self.status_pass)
        self.assertEqual("<TestStatus: Pass>", sp_str)

        sf_str = str(self.status_fail)
        self.assertEqual("<TestStatus: Fail>", sf_str)

