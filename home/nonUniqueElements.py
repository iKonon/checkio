'''
You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].

Input: A list of integers.
Output: The list of integers.

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

Precondition:
0 < len(data) < 1000
'''

def checkioNaive(alist):
    output = []
    for x in alist:
        if alist.count(x) != 1:
            output.append(x)
    return output

def checkioSmart(alist):
    # return list(filter(lambda x: alist.count(x) > 1, alist))
    return [n for n in alist if alist.count(n) > 1]

def checkio(data): # O(n)
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]

# checkio = lambda d:[x for x in d if d.count(x) > 1]

if __name__ == '__main__':
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
