Implement a infixToPostfixEval function that takes in a string representing a mathematical expression in infix notation 
and returns two things: a string representing the expression in postfix notation and its value. 
Valid operands consist of the digits 0 to 9, 
and operators are the operators (, ), +, -, *, /, and the unary factorial operator !. 
Assume there are no errors, i.e., invalid or misplaced operands or operators, in the input string.
Implement infixToPostfixEval as a direct infix evaluator that combines the functionality of theinfixToPostfix function 
and the postfix evaluation algorithm. 
Your infixToPostfixEval should process infix tokens from left to right and, 
while processing those tokens, use two stacks, one for operators and one for operands, to perform the evaluation. 
