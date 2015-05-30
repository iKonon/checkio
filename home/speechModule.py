'''
Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.

Example:

checkio(4)=='four'
checkio(143)=='one hundred forty three'
checkio(12)=='twelve'
checkio(101)=='one hundred one'
checkio(212)=='two hundred twelve'
checkio(40)=='forty'

How it is used: This concept may be useful for the speech synthesis software or automatic reports systems. This system can also be used when writing a chatbot by assigning words or phrases numerical values and having a system retrieve responses based on those values.

Precondition: 0 < number < 1000
'''
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number > 99: 
        if number%100 == 0: return FIRST_TEN[number//100 - 1] + " " + HUNDRED
        else: return FIRST_TEN[number//100 - 1] + " " + HUNDRED + " " + checkio(number - (number//100)*100)
        
    if number > 19:
        if number%10 == 0: return OTHER_TENS[number//10 - 10]
        else: return OTHER_TENS[number//10 - 10] + " " + checkio(number - (number//10)*10)
    
    if (number > 9):
        return SECOND_TEN[number-10]       
    
    if number < 10:
        return FIRST_TEN[number-1]
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"