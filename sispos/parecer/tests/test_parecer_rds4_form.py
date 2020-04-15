from django.test import TestCase
from sispos.parecer.forms import Rds4Form


class Rds4FormTest(TestCase):
    def setUp(self):
        self.form = Rds4Form()

    def test_rds_attr(self):
        """Rds4Form must have attr"""
        attrs = ['perspectiva', 'status']
        for expected in attrs:
            with self.subTest():
                self.assertIn(expected, list(self.form.fields))
