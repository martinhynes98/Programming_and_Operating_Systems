##Martin Hynes
##16390836

##Task 1
import time
import sys
##setting recursion limit for testing large numbers of n later
sys.setrecursionlimit(1000000)
##f, 2**n
##Using recursion for benefit of memoization
def f(n):
    ##anything to power of 0 is 1
    if n==0:
        return 1
    ##2 to power of 1 is 2
    elif n==1:
        return 2
    ##2 to power of n = 2*2 to power of n-1
    else:
        return 2*f(n-1)

##g: g(n) = g(n-1)+2*g(n-2)
def g(n):
    ##g(0)==0
    if n == 0:
        return 0
    ##g(1)==1
    elif n==1:
        return 1
    ##g(n)== g(n-1)+2*g(n-2)
    else:
        return (g(n-1)*(g(n-1)+(2*(g(n-2)))))

##Task 2
##Function F
##n=1000: memoized function is approx .0005 seconds quicker
##n=750:  memoized function approx .00048 seconds quicker
##n=2500: memoized function approx .0015 seconds quicker
##Function G
##n=20: memoized function is approx 6.8 seconds quicker
##n=22: memoized function approx 39 seconds quicker
##n=25: memoized function approx 1.15 seconds quicker

#basic memoize function
def memoize(f):
    #stores results in cache dictionary
    cache = {}
    #helper function to fill cache
    def helper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return helper

##applying memoize function to mf, a duplicate of f
@memoize
def mf(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return 2*mf(n-1)


##applying memoize function to mg, a duplicate of g
@memoize
def mg(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return mg(n-1)*(mg(n-1)+(2*(mg(n-2))))

##Loops I used for checking times for both functions
print("Function F:")
for i in range(20):
    a = time.time()
    f(1000)
    b = time.time()
    mf(1000)
    c = time.time()
    if (c-b) < (b-a):
        print("memoized function was",(b-a)-(c-b),"seconds quicker")
    elif (c-b)==(b-a):
        print("Both functions took approx the same time.")
    else:
        print("regular function was",(c-b)-(b-a),"seconds quicker")

print("\nFunction G:")
for i in range(20):
    a = time.time()
    g(20)
    b = time.time()
    mg(20)
    c = time.time()
    if (c-b) < (b-a):
        print("memoized function was",(b-a)-(c-b),"seconds quicker")
    elif (c-b)==(b-a):
        print("Both functions took approx the same time.")
    else:
        print("regular function was",(c-b)-(b-a),"seconds quicker")
