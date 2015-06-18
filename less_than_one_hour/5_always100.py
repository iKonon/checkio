'''
Write a program that outputs all possibilities to put + or - or nothing 
between the numbers 1, 2,..., 9 (in this order) such that the result is always 100.
For example: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100
'''

def get_sequences(sequence,digit):
    if digit <= 9: 
        [get_sequences(sequence+x+str(digit),digit+1) for x in("+","-","")]
    elif eval(sequence)==100: 
        print(sequence + " = " + str(eval(sequence)))

def get_sequences_itertools():
    from itertools import product
    results, numbers = [], range(1, 10)
    for permutation in product(['+','-', ''], repeat=8):
        tuples = zip(numbers, permutation + ('', ))
        sequence = ''.join([str(e1) + e2 for (e1, e2) in tuples])
        if eval(sequence) == 100:
            results.append(sequence + ' = 100')
    return results

if __name__ == '__main__':            
    get_sequences("1",2)
    assert len(get_sequences_itertools()) == 11

'''
others:
http://stackoverflow.com/questions/30134535/how-to-use-prolog-constraints
https://www.snip2code.com/Snippet/502651/Write-a-program-that-outputs-all-possibi
https://gist.github.com/prosseek/41201d6508f01cf1643e
'''