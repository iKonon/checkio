'''
In computer science and discrete mathematics, an inversion is a pair of places in a sequence 
where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, 
then an inversion is when larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions - 5 and 3; - 5 and 4; - 7 and 6.

You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

Input: A sequence as a tuple of integers.
Output: The inversion number as an integer.

How it is used: In this mission you will get to experience the wonder of nested loops, 
that is of course, if you don't use advanced algorithms.

Precondition: 2 < len(sequence) < 200, len(sequence) == len(set(sequence)), all(-100 < x < 100 for x in sequence)
'''

def count_inversion(sequence):
    # Count inversions in a sequence of numbers
    count = 0
    for i in range(len(sequence)):
        for j in range(i,len(sequence)):
            if sequence[j] < sequence[i]:
                count += 1 
        
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
