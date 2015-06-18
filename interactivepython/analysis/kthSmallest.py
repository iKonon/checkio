'''
Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
Can you improve the algorithm from the previous problem to be linear? Explain.

Example: Suppose that the following array with 5 numbers is given: 3, 1, 7, 5, 9. 
For K=3, the result is 7. This is because, when array is sorted into 1, 3, 5, 7, 9, the element at zero-based position 3 is number 7.

It is possible to find the k smallest of n elements in O(n) time. 
Refer to the Wikipedia article "Selection algorithm", 
especially the subsections on "unordered partial sorting" and "median selection as pivot strategy", 
and also to the article "Median of medians" for the essential piece that makes this O(n).
'''
import random

# In a simple way we can use a sorting algorithm initially probably a O(n log n) algorithm 
# and then finding a median or kth smallest element is a trivial matter
def kth_smallest_simple(alist, k):
    sortedlist = sorted(alist)
    return sortedlist[k]

# O(kn) algorithm
def kth_smallest_partial_selection_sort(alist, k):
    for i in range(k):
        minIndex = i
        minValue = alist[i]
        for j in range(i, len(alist)):
            if alist[j] < minValue:
                minIndex = j
                minValue = alist[j]
        alist[i], alist[minIndex] = alist[minIndex], alist[i] # swap(alist[i], alist[minIndex])
    return alist[k]

# O(n) algorithm
def kth_smallest_linear(alist, k):
    pivot = alist[random.randint(0, len(alist)-1)]
    # lesser and bigger array
    below = [x for x in alist if x < pivot] # for x in range (0,len(alist)): if alist[x] < pivot: left.append(alist[x])
    above = [x for x in alist if x > pivot]
    i, j = len(below), len(alist)-len(above)

    if k < i: 
        return kth_smallest_linear(below, k)
    elif k >= j: 
        return kth_smallest_linear(above, k-j)
    else:
        return pivot
    
if __name__ == '__main__':
    alist = [3, 1, 7, 5, 9]
    assert kth_smallest_simple(alist, 3) == 7
    assert kth_smallest_partial_selection_sort(alist,3) == 7
    assert kth_smallest_linear(alist,3) == 7
    
    sample = [random.random() for _ in range(1000)]
    k = random.choice(range(1000))
    print(kth_smallest_linear(sample,k))