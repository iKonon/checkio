'''
"Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5; 
The number as a string for other cases.

Input: A number as an integer.

Output: The answer as a string.
'''

def fizz_buzz(n):
    if n%15 == 0: # 15 divided by 3 and 15
        return "Fizz Buzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return None
        
if __name__ == "__main__":
    assert(fizz_buzz(15)) == "Fizz Buzz"
    assert(fizz_buzz(6)) == "Fizz"
    assert(fizz_buzz(5)) == "Buzz"
