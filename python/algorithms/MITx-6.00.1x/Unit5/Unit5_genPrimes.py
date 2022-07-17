'''
Write a generator, genPrimes, that returns the sequence of 
prime numbers on successive calls to its next() method: 2, 
3, 5, 7, 11, ...

Hints
Ideas about the problem

Have the generator keep a list of the primes it's generated. 
A candidate number x is prime if (x % p) != 0 for all earlier
 primes p.
 
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
'''

def genPrimes():
    a = 2
    
    while True:
        pr = True
        for n in range(2, a):
            if a % n == 0:
                pr = False
                break
        if pr:
            yield a
        a += 1


def funPrimes():
    primes = []
    
    a = 2
    while True:
        pr = True
        for n in range(2, a):
            print('a: ', a)
            if a % n == 0:
                pr = False
                break
        if pr:
            primes.append(a)
        a += 1
        if a > 40:
            break
    return primes

print(funPrimes())
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    