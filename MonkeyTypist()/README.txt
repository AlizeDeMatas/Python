The Infinte Monkey Theorem states that a monkey hitting keys at random on a typewriter keyboard for an 
infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare.

Well, suppose we replace a monkey with a Python function. 
How long do you think it would take for a Python function to generate just one sentence of Shakespeare? 
The sentence we’ll shoot for is: “methinks it is like a weasel”.

The monkeyTypist() function uses two helper functions: generate_string() and score_string().
monkeyTypist function will keep letters that are correct and only modifies one character in the best string so far. 
The monkeyTypist function produces the following output: print the best string and its score, 
every 100 tries, and plots a graph showing the scores of the best strings found and the iteration in which they were found. 
The x-axis represents the iteration number, and the y-axis represents the scores of the best strings.
