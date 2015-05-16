'''
Write a function that combines two lists by alternatingly taking elements. 
For example: given the two lists [a, b, c] and [1, 2, 3], 
the function should return [a, 1, b, 2, c, 3].
'''

def combineAlternatingSlice(A,B):
    D = [None]*(len(A)+len(B))
    D[::2] = A
    D[1::2] = B
    return D

def combineAlternatingZip(A,B):
    F = []
    for item in zip(A, B):
        F.extend(item)
    return F

def combineAlternatingZipEnhanced(A,B):    
    E = [y for x in zip(A, B) for y in x]
    return E

def combineAlternatingItertools(A,B):
    from itertools import chain
    return [x for x in chain.from_iterable(zip(A, B))]

def combineAlternatingNumpy(A,B):
    import numpy as np
    C = np.insert(B, np.arange(len(A)), A) # change output format
    return C

if __name__ == '__main__':
    assert combineAlternatingSlice(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
    assert combineAlternatingZip(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
    assert combineAlternatingZipEnhanced(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3] 
    assert combineAlternatingItertools(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
#   assert combineAlternatingNumpy(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]