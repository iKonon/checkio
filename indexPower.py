'''
You are given an array with positive numbers and a number N.
You should find the N-th power of the element in the array with the index N.
If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.
Output: The result as an integer.

Precondition: 0 < len(array) <= 10; 0 <= N; all(0 <= x <= 100 for x in array)
'''

def indexPower(array, N):
    if -1 < len(array) > 100 or -1 < N > len(array)-1:
        return -1
    else:
        return array[N]**N

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert indexPower([1, 2, 3, 4], 2) == 9
    assert indexPower([1, 3, 10, 100], 3) == 1000000
    assert indexPower([0, 1], 0) == 1
    assert indexPower([1, 2], 3) == -1
    assert indexPower([96, 92,94], 3) == -1
    assert indexPower([5], 0) == 1