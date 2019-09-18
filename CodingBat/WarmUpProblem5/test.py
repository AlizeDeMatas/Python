import unittest
from mySolution import parrot_trouble

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

class test__init__(unittest.TestCase):
    def test_parrot_trouble(self):
        talking = True
        hour = 6
        self.assertTrue(parrot_trouble(talking == True, hour < 7 or hour > 20))
        self.assertFalse(parrot_trouble(talking == False, hour > 7 or hour < 20))

if __name__ == '__main__':
    unittest.main()
