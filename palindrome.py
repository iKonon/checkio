"""
Check if string is palindrome
"""

def palindrome(word):
    return word.replace(" ", "") == word.replace(" ", "")[::-1]
    
if __name__ == '__main__':
    assert palindrome('step on no pets') == True
    assert palindrome('eva can i see bees in a cave') == True
    assert palindrome('robert trebor') == True
    assert palindrome('palindrome') == False