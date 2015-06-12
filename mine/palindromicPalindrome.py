'''
Write a palindromic program with a checkio(s) function that checks whether s (a string) is a palindrome.
For this task, using "#" is forbidden.
You can use other methods for the function's definition (for example a lambda). 
The test will try to run the function "checkio" from your code.

The example of the palindromic code: checkio=lambda x: x#x :x adbmal=oikcehc
However, in your code, you can not use "#".

Input: A text as a string.
Output: Palindrome or not as a boolean.

How it is used: This task is a challenge in creativity and is designed to show you the hidden depths of programming languages.
Precondition: 1 < |text| <= 20
The text contains only ASCII letters in lowercase.
'''
    
""" ";]1-::[x == x:x adbmal=oikcehc;""";checkio=lambda x:x == x[::-1];" """

def palindrome(word):
    return word.replace(" ", "") == word.replace(" ", "")[::-1]
    
if __name__ == '__main__':
    print(checkio('step on no pets'))
    assert palindrome('step on no pets') == True
    assert palindrome('eva can i see bees in a cave') == True
    assert palindrome('robert trebor') == True
    assert palindrome('palindrome') == False