import unittest
from mySolution import infixToPostfixEval

class Test__init__(unittest.TestCase):
    # Test infix to post and finally evaluate function
    def test_infixToPostfixEval(self):
        self.assertEqual(infixToPostfixEval('4 + 3'), ('4 3 +', 7))
        self.assertEqual(infixToPostfixEval('4 - 3'), ('4 3 -', 1))
    # Test to see if function works with brackets
    def test_Brackets(self):
        self.assertEqual(infixToPostfixEval('( 5 - 3 ) * 7'), ('5 3 - 7 *', 14))
        self.assertEqual(infixToPostfixEval('( 5 + 3 ) * 7'), ('5 3 + 7 *', 56))
    # Test to see if function works with factorial
    def test_Factorial(self):
        self.assertEqual(infixToPostfixEval('( 4 + 4 ) ! + 8'), ('4 4 + ! 8 +', 40328))
    # Test to see correct precedence
    def test_precedence(self):
        self.assertEqual(infixToPostfixEval('( 5 + 3 ) * 2'), ('5 3 + 2 *', 16))
    # Test to see negative output
    def test_negativeOutput(self):
        self.assertEqual(infixToPostfixEval('( 4 - 5 ) * 1'), ('4 5 - 1 *', -1))



if __name__ == '__main__':
    unittest.main()
