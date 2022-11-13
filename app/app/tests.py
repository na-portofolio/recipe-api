"""
sample test
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """Test adding numbers together."""
        res = calc.add(2, 3)

        self.assertEqual(res, 5)

    def test_substract_number(self):
        """Test substract numbers together."""
        res = calc.substract(2, 4)

        self.assertEqual(res, 2)
