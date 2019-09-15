import matplotlib.pyplot as plt
import random

target = "methinks it is like a weasel"

   # generates a random string of characters that are the same length as target
def generate_string(strLen):
    alphabet = list("abcdefghiljklmnopqrstuvwxyz ")
    test_string = ""
    for i in range(strLen):
        test_string = test_string + alphabet[random.randrange(27)]
    return test_string

   # keep tracks to see which string is better than the other one using a scoring system
   # iterate through all the characters in the generated string, if they match the target, give it a point
def score_string(test_string, target_string):
    score = 0
    for i in range(len(target_string)):
        if target_string[i] == test_string[i]:
            score += 1
    return score

def monkeyTypist():
    y = []
    x = []
    lenS = len(target)
    alphabet = list("abcdefghijklmnopqrstuvwxyz ")
    lenA = len(alphabet)
    counter = 0
    bestStr = generate_string(lenS)
    bestScore = score_string(bestStr, target)
    print("String                       Score")
    while bestScore < 28:
        if bestScore == 28:
            break
        newStr = generate_string(lenS)
        newScore = score_string(newStr, target)
        for i in range(lenS):
            while target[i] != newStr[i]:
                c = alphabet[random.randrange(27)]
                newStr = newStr[:i] + c + newStr[i+1:]
                counter += 1
                bestScore = score_string("".join(newStr), "".join(target))
                if counter % 100 == 0:
                    x = x + [counter]
                    y = y + [bestScore]
                    print("%s      %d     %d" % ("".join(newStr), bestScore,counter))
    print("Found a perfect match")
    print("%s      %d     %d" % ("".join(newStr), bestScore, counter))
    plt.scatter(x, y)
    plt.show()
monkeyTypist()
