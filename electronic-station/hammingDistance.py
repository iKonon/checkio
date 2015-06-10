'''
The Hamming distance between two binary integers is the number of bit positions that differs 
(read more about the Hamming distance on Wikipedia: http://en.wikipedia.org/wiki/Hamming_distance). 
For example:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

You are given two positive numbers (N, M) in decimal form. 
You should calculate the Hamming distance between these two numbers in binary form.

Input: Two arguments as integers.
Output: The Hamming distance as an integer.

How it is used: This is a basis for Hamming code and other linear error-correcting programs. 
The Hamming distance is used in systematics as a measure of genetic distance. 
On a grid (ie: a chessboard,) the Hamming distance is the minimum number of moves it would take a rook to move from one cell to the other.

Precondition: 0 < n < 10^6; 0 < m < 10^6
'''

def checkio(n, m):
    bN = bin(n)[2:]
    bM = bin(m)[2:]
    if len(bN) > len(bM):
        bM = bM.zfill(len(bN))
    else:
        bN = bN.zfill(len(bM))
    
    counter = 0
    for i in range(len(bN)):
        if bN[i] != bM[i]:
            counter += 1
    return counter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
