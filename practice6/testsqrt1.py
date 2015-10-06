import unittest
import lib
class LibTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(lib.sqrt(4),2)
        self.assertEqual(lib.sqrt(16),4)
        self.assertNotEqual(lib.sqrt(540),10)
        self.assertNotEqual(lib.sqrt(64),7)
def test_sqrt_negative(self):
        self.assertEqual(lib.sqrt(-1), 0)
unittest.main(verbosity=2)