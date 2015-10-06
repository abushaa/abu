import unittest
import lib
import math
class LibTest(unittest.TestCase):
    def test_sin(self):
        self.assertEqual(lib.sin(math.pi),0)
        self.assertEqual(lib.sin(math.pi/2), 1)
        self.assertNotEqual(lib.sin(0), 1)
        self.assertNotEqual(lib.sin(18), 6)
unittest.main(verbosity=2)