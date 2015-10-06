import unittest
import lib
class LibTest(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(lib.palindrome('151'),True)
        self.assertEqual(lib.palindrome('626'), True)
        self.assertEqual(lib.palindrome('0'), True)
        self.assertEqual(lib.palindrome('187'), False)
unittest.main(verbosity=2)