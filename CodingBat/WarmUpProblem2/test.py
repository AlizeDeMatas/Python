import unittest
from mySolution import monkey_trouble

class Test__init__(unittest.TestCase):
    # Tester
    # monkey_trouble(True, True) -> True
    # monkey_trouble(False, False) -> True
    # monkey_trouble(True, False) -> False
    def test_monkey_trouble(self):
        a_smile = True
        b_smile = True

        self.assertTrue(monkey_trouble(a_smile, b_smile))
        self.assertTrue(monkey_trouble(not a_smile, not b_smile))
        self.assertFalse(monkey_trouble(a_smile, not b_smile))

if __name__ == '__main__':
    unittest.main()
