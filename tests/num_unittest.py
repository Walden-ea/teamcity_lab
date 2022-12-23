import num
# import pytest

# assert(num.get_num(5)==7)

# assert(num.get_num(7)==7)

# assert(num.get_num(5)!=1)

# assert(num.get_num(10)!=10)

import unittest

class TestSum(unittest.TestCase):

    def test_5(self):
        self.assertEqual(num.get_num(5), 7, "Should be 7")

    def test_7(self):
        self.assertEqual(num.get_num(7), 7, "Should be 7")

    def test_fail(self):
        self.assertNotEqual(num.get_num(7),1, "Should be not 1")


if __name__ == '__main__':
    unittest.main()