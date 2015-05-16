'''
Write a function that given a list of non negative integers, 
arranges them such that they form the largest possible number. 
For example, given [50, 2, 1, 9], the largest formed number is 95021.
'''

def arrangeMax(array):
    def comparison(x,y):
        sx = str(x)
        sy = str(y)
        sx = sx + sy
        sy = sy + sx
        if sx > sy: return -1
        if sx <= sy: return 1
            
    sorted_array = sorted(array, cmp=comparison)
    return int(''.join([str(n) for n in sorted_array]))

def arrangeMax2(array):    
    array = sorted(array, reverse=True) #From largest to smallest 
    n = max([len(str(x)) for x in array])
    def concatenation(x):
        x = str(x)
        x *= int(n/len(x)) + 1
        return int(x[0:n])
    array = sorted(array,key=concatenation,reverse=True)
    return int(''.join(map(str,array)))

if __name__ == '__main__':
    assert arrangeMax([50, 2, 1, 9]) == 95021
    assert arrangeMax([5, 50, 56]) == 56550
    assert arrangeMax2([50, 2, 1, 9]) == 95021
    assert arrangeMax2([5, 50, 56]) == 56550    