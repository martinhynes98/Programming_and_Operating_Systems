##Martin Hynes
##16390836

import math
##Task 1
##Define function
def fact(n):
    ##if n is 0, reurn 1
    if n == 0:
        return 1
    ##return n * fact(n-1) for n>0
    else:
        return n*fact(n-1)
    ##Return factorial result


##Task 2
##Define function
def powTwo(x):
    ##Return 2 to power of x
    return 2**x

##Task 3
##Define function
def commute(f,g):
    ##define combine function
    def combine(f,g):
        ##use lambda function to create f(g(x))
        a = lambda x: f(g(x))
        ##use lambda function to create g(f(x))
        b = lambda x: g(f(x))
        ##use lambda function to create function which is fg - gf
        c = lambda x: a(x) - b(x)
        ##return final function
        return c
    ##return fg - gf function
    return combine(f,g)

##Task 4

##commute(fact,powTwo)(3) = 40256
##commute(powTwo,fact)(4) = -20922773110784
