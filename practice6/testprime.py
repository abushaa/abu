import unittest
import lib
class LibTest(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(lib.prime(7),True)
        self.assertEqual(lib.prime(17), True)
        self.assertEqual(lib.prime(540), False)
        self.assertEqual(lib.prime(18), False)
unittest.main(verbosity=2)