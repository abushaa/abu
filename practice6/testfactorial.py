import unittest
import lib
class LibTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(lib.factorial(7), 5040)
        self.assertEqual(lib.factorial(2), 2)
        self.assertNotEqual(lib.factorial(40),6700)
        self.assertNotEqual(lib.factorial(5), 8)
    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-1), 1)
        self.assertEqual(lib.factorial(-7), 1)
unittest.main(verbosity=2)
