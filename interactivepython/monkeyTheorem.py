'''
Self Check
Here's a self check that really covers everything so far. You may have heard of the infinite monkey theorem? 
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time 
will almost surely type a given text, such as the complete works of William Shakespeare. 
Well, suppose we replace a monkey with a Python function. 
How long do you think it would take for a Python function to generate just one sentence of Shakespeare? 
The sentence we'll shoot for is: "methinks it is like a weasel"

The way we'll simulate this is to write a function that generates a string that is 27 characters long 
by choosing random letters from the 26 letters in the alphabet plus the space. 
We'll write another function that will score each generated string by comparing the randomly generated string to the goal.
A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. 
If the letters are not correct then we will generate a whole new string.
To make it easier to follow your program's progress this third function should print out the best string generated so far 
and its score every 1000 tries.

Self Check Challenge
See if you can improve upon the program in the self check by keeping letters that are correct 
and only modifying one character in the best string so far. 
This is a type of algorithm in the class of 'hill climbing' algorithms, 
that is we only keep the result if it is better than the previous one.
'''
# http://evoinfo.org/weasel.html
# http://like-a-weasel.blogspot.com

import random

def generate_string(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    return "".join(random.choice(alphabet) for _ in range(size))

def get_score(goal, guess):
    if guess == goal:
        return 1
    else:
        count = 0
        for x in range(len(goal)):
            if guess[x] == goal[x]:
                count += 1
        return float(count)/len(goal)

def monkey_typing(goal):
    guess = generate_string(28)
    score = get_score(goal, guess)
    i = 0

    while (score < 1):
        if i == 100000:
            break
        if not(i % 1000):
            print("Best so far: %s (score %d) %i iterations" % (guess, score, i))
        guess = generate_string(28)
        score = get_score(goal, guess)
        i += 1
    return guess
        
def smart_monkey(goal):
    guess = generate_string(len(goal))
    score = get_score(goal, guess)
    i, max = 0, 0   
    best = ""
    matching = [""]*len(goal)
    
    while (score < 1):
        goal = list(goal)
        guess = list(guess)
        for x in range(len(goal)):
            if guess[x] == goal[x]:
                matching[x] = guess[x]
            else:
                matching[x] = generate_string(1)
        goal = "".join(goal)
        guess = "".join(matching)
        score = get_score(goal, guess) 
        i += 1
        #climb a hill
        if score > max:
            max = score
            best = guess
        if not(i % 100):
            print("Best so far: %s (score %f) %i iterations" % (best, score, i))
    return i        

if __name__ == '__main__':
    goal = "methinks it is like a weasel"
    print("Monkey is typing to get the following text: %s" % goal)
    print("Well done after %i iterations!" % smart_monkey(goal))