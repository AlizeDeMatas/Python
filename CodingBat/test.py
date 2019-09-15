import unittest
from mySolution import sleep_in


class Test_warmUp1(unittest.TestCase):
    def test_sleep_in(self):
        # sleep_in(False, False) -> True
        # sleep_in(True, False) -> False
        # sleep_in(False, True) -> True
        self.assertTrue(weekday(False),vacation(False))
        #self.assertFalse(True, False)
        #self.assertTrue(False, True)

if __name__ == '__main__':
    unittest.main()
