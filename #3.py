import math
n = 600851475143
fac = []
for i in range(2,math.ceil(math.sqrt(n))):
    if n%i==0:
        fac.append(i)
        n=n/i
print(fac)