'''
Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. 
As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
'''

def fibonacci_naive(n):
    if n == 0: return 0
    a,b = 1,1
    for iter in range(n-1):
        a,b = b,a+b
    return a

def fibonacci_recursive(n):
    if n == 0: return 0
    if n==1 or n==2: return 1
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

def fibonacci_100_naive():
    return [str(fibonacci_naive(i)) for i in range(100)]

# using generators
def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def fibonacci_100():
    tmp = fibonacci()
    return [tmp.next() for _ in range(100)] 

if __name__ == '__main__':
    assert len(fibonacci_100()) == 100
    assert len(fibonacci_100_naive()) == 100    
    #for i in range(10): print(fibonacci_recursive(i))