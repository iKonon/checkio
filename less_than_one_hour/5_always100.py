'''
Write a program that outputs all possibilities to put + or - or nothing 
between the numbers 1, 2,..., 9 (in this order) such that the result is always 100.
For example: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
'''

def getSequences(sequence,digit):
    if digit <= 9: 
        [getSequences(sequence+x+str(digit),digit+1) for x in("+","-","")]
    elif eval(sequence)==100: 
        print(sequence + " = " + str(eval(sequence)))

if __name__ == '__main__':            
    getSequences("1",2)

'''
others:
http://stackoverflow.com/questions/30134535/how-to-use-prolog-constraints
https://www.snip2code.com/Snippet/502651/Write-a-program-that-outputs-all-possibi
https://gist.github.com/prosseek/41201d6508f01cf1643e
'''