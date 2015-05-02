'''
You are given an array of integers. 
You should find the sum of the elements with even indexes (0th, 2nd, 4th...) 
then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.
Example:
checkio([0, 1, 2, 3, 4, 5]) == 30
checkio([1, 3, 5]) == 30
checkio([6]) == 36
checkio([]) == 0

How it is used: Indexes and slices are important elements of coding in python and other languages. 
This will come in handy down the road!

Precondition: 0 <= len(array) <= 20; all(isinstance(x, int) for x in array); all(-100 < x < 100 for x in array)
'''

def evenTheLast(array):
    # sums even-indexes elements and multiply at the last
    if array:
        return sum(array[::2]) * array[-1]
    return 0

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert evenTheLast([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert evenTheLast([1, 3, 5]) == 30, "(1+5)*5=30"
    assert evenTheLast([6]) == 36, "(6)*6=36"
    assert evenTheLast([]) == 0, "An empty array = 0"