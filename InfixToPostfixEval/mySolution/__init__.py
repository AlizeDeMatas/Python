
from pythonds.basic import Stack
import math


# Take an infix expression, convert it to postfix and finally evaluate it
def infixToPostfixEval(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["!"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    output: ""

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            topToken = opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                   postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        output = " ".join(postfixList)
        operandStack = Stack()
        str1 = " ".join(postfixList)
        tokenLists = str1.split()

        for token in tokenLists:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                if token == "!":
                    result = math.factorial(operandStack.pop())

                else:
                    operand2 = operandStack.pop()
                    operand1 = operandStack.pop()
                    result = doMath(token, operand1, operand2)
                operandStack.push(result)
        return output, operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print('Infix Expression : ( 2 + 2 ) ! + 8')
x,y = infixToPostfixEval('( 2 + 2 ) ! + 8')
print(x, "\nEvaluates to: ", + y)