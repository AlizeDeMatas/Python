import unittest
from mySolution import near_hundred

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False
class testnear_hundred(unittest.TestCase):
    def test_something(self):
        n = 93
        self.assertTrue(near_hundred(n))
        #
        # self.assertTrue(near_hundred(90))
        #self.assertFalse(near_hundred(89))


if __name__ == '__main__':
    unittest.main()
