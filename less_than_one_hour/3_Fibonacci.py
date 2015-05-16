'''
Write a function that computes the list of the first 100 Fibonacci numbers. 
By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
and each subsequent number is the sum of the previous two. 
As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
'''

def FibonacciNaive(n):
    if n == 0: return 0
    a,b = 1,1
    for iter in range(n-1):
        a,b = b,a+b
    return a

def FibonacciRecursion(n):
    if n == 0: return 0
    if n==1 or n==2: return 1
    return FibonacciRecursion(n-1)+FibonacciRecursion(n-2)

def Fibonacci100Naive():
    return [str(FibonacciNaive(i)) for i in range(100)]

# using generators
def Fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

def Fibonacci100():
    tmp = Fibonacci()
    return [tmp.next() for _ in range(100)] 

if __name__ == '__main__':
    assert len(Fibonacci100()) == 100
    assert len(Fibonacci100Naive()) == 100    
    #for i in range(10): print(FibonacciRecursion(i))