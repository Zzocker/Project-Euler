def no_divisor(n):
    m = 0
    for i in range(1,n//2+1):
        if n%i==0:
            m+=1
    return m +1
j= 0
n=0
while no_divisor(n) in range(500):
    j += 1
    n = (j*(j+1))//2

print(j)
print(n)




