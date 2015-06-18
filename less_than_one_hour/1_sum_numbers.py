'''
From: https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Write three functions that compute the sum of the numbers in a given list 
using a for-loop, a while-loop, and recursion.
'''

def sum_with_for(array):
    summ = 0
    for item in array:
        summ += item
    return summ

def sum_with_while(array):
    summ, i = 0, 0
    while i < len(array):
        summ += array[i]
        i += 1
    return summ

def sum_recursive(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_recursive(array[1:])    

def sum_recursive_iter(array, summ = 0):
    if len(array):
        i = iter(array)
        summ += i.next()
        return sum_recursive_iter(list(i), summ)
    else:
        return summ
    
if __name__ == '__main__':
    assert sum_with_for([1,2,3]) == sum([1,2,3])
    assert sum_with_while([-1,-2,3]) == sum([-1,-2,3])
    assert sum_recursive([1,2,3,5,6]) == sum([1,2,3,5,6])   
    assert sum_recursive_iter([1,2,3,10]) == sum([1,2,3,10])            