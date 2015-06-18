'''
Write a function that combines two lists by alternatingly taking elements. 
For example: given the two lists [a, b, c] and [1, 2, 3], 
the function should return [a, 1, b, 2, c, 3].
'''

def combine_alternating_slice(A,B):
    D = [None]*(len(A)+len(B))
    D[::2] = A
    D[1::2] = B
    return D

def combine_alternating_zip(A,B):
    F = []
    for item in zip(A, B):
        F.extend(item)
    return F

def combine_alternating_zip_enhanced(A,B):    
    E = [y for x in zip(A, B) for y in x]
    return E

def combine_alternating_itertools(A,B):
    from itertools import chain
    return [x for x in chain.from_iterable(zip(A, B))]

def combine_alternating_numpy(A,B):
    import numpy as np
    C = np.insert(B, np.arange(len(A)), A) # change output format
    return C

if __name__ == '__main__':
    assert combine_alternating_slice(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
    assert combine_alternating_zip(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
    assert combine_alternating_zip_enhanced(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3] 
    assert combine_alternating_itertools(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
#   assert combineAlternatingNumpy(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]