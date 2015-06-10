'''
Help Stephen to create a module for converting a normal time string to a morse time string. 
As you can see in the illustration, a gray circle means on, while a white circle means off. 
Every digit in the time string contains a different number of slots. 
The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. 
The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. 
Every digit in the time is converted to binary representation. 
You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").

example source: http://en.wikipedia.org/wiki/Binary_clock

An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The "missing" digits are zeroes. 
For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format: "h h : m m : s s" where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).
Output: The morse time string as a string.

How it is used: Did you see the binary clocks task earlier? This is can be a fun gift for any geek. 
We tried to combine the old good Morse code with a binary clock in this task, and now you can create the new more complex binary clock, 
which doesn't show time -- but makes morse style bips and beeps. ;-)

Precondition: time_string contains correct time.
'''
from string import maketrans

def checkio1(time_string):
    alist = []
    for x in time_string.split(":"):
        alist.extend([str(bin(int(d)))[2:] for d in x.zfill(2)])

    output = "{:0>2s} {:0>4s} : {:0>3s} {:0>4s} : {:0>3s} {:0>4s}".format(*alist) # convert each digit to binary
    return output.translate(maketrans("01", ".-"))

def checkio(data):
    fmt = "{:0>2b} {:0>4b} : {:0>3b} {:0>4b} : {:0>3b} {:0>4b}"
    ns = [int(x) for x in ''.join(n.zfill(2) for n in data.split(':'))]
    return fmt.format(*ns).replace('0', '.').replace('1', '-')

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"