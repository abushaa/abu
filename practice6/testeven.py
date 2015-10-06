import unittest
import lib
class LibTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(lib.even(9), False)
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(40), True)
        self.assertEqual(lib.even(87), False)
unittest.main(verbosity=2)
