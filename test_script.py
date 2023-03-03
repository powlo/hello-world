from unittest import TestCase
from script import get_hello


class ScriptTestCase(TestCase):
    def test_simple(self):
        self.assertEqual("Hello Robin!", get_hello("Robin"))
