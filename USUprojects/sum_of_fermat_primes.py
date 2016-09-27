#!/usr/bin/python
from random import randint
def is_even(n): return n % 2 == 0

def square(n): return n**2

def expmod(base, exp, modu):
    ##your code
    if (exp==0):
        return 1
    elif (is_even(exp)):
        expm = expmod(base,exp/2, modu)
        return (expm*expm)%modu
    else:
        return (base*expmod(base,exp-1, modu))%modu
    
def fermat_test(n):
    if n < 3:
        if n == 2:
            return True
        a = 2
    else:
        a = randint(2, n-1)  
    return expmod(a,n,n)==a
    
def is_fermat_prime(n, ntimes):
    if (ntimes ==0):
        return True
    elif (fermat_test(n)):
        return is_fermat_prime(n, ntimes-1)
    else:
        return False
    ## your code

    
## This is the test you can use to test your code
def sum_of_fermat_primes(n):
    sum = 0
    for i in xrange(n+1):
        if is_fermat_prime(i, 70):
            sum += i
    return sum


print sum_of_fermat_primes(10)
print sum_of_fermat_primes(20)
print sum_of_fermat_primes(560)
print sum_of_fermat_primes(570)
    
