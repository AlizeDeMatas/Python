import unittest
from mySolution import generate_string
from mySolution import score_string

target = "methinks it is like a weasel"

class Test_init_(unittest.TestCase):
    def test_generate(self):
        # Test the strings generated are random
        self.assertFalse(generate_string(28) == generate_string(28))

    def test_score(self):
        # Test the score is correct, compare the target to the string generated, check if code score is correct
        self.assertEqual(score_string("methinks it is like a weasel","methinks it is like a weasel"), 28)

if __name__ == '__main__':
    unittest.main()
