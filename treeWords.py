'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
'''

def checkio(words):
    count = 0
    words = words.split()
    for word in words:
        if word.isalpha():
            count += 1
        else:
            count = 0
    if count > 2: return True
    else:  return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True
    assert checkio("He is 123 man") == False
    assert checkio("1 2 3 4") == False
    assert checkio("bla bla bla bla") == True
    assert checkio("Hi") == False

'''
import re
def only_letters(word):
    match = re.match("^[A-z]*$", word)
    return match is not None
'''
