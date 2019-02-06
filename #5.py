from math import factorial as fac
def is_multiple(x,n):
    for i in range(2,n):
        if x%i!=0:
            return False

    return True
def lest_multiple(n):
    for i in range(n,fac(n)+1,n):
        if is_multiple(i,n):
            return i

print(lest_multiple(10))
