import unittest
from mySolution import diff21
# Tester
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0


class test__init__(unittest.TestCase):
    def test_def21(self):
        n = 5
        if self.assertLessEqual( diff21(n) , 21):
            return abs(21 - n)
        else:
            return 2 * abs(21 - n)

if __name__ == '__main__':
    unittest.main()
