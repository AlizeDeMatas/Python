import unittest
from mySolution import sleep_in

# Tester
class Test__init__(unittest.TestCase):
    def test_sleep_in(self):
        weekday = True
        vacation = True
        # sleep_in(False, False) -> True
        # sleep_in(True, False) -> False
        # sleep_in(False, True) -> True
        self.assertTrue(sleep_in(not weekday, not vacation))
        self.assertFalse(sleep_in(weekday, not vacation))
        self.assertTrue(sleep_in(not weekday, vacation))

if __name__ == '__main__':
    unittest.main()
