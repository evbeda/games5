import unittest
from ..rummy_and_burakko import RummyAndBurakko
from parameterized import parameterized


class TestRummyAndBurakko(unittest.TestCase):
    def setUp(self):
        self.rummy = RummyAndBurakko()

    def test_init(self):
        x = self.rummy.probando()
        self.assertEqual(x, "anda")
