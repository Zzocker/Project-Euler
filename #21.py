def devi(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
n = int(input())
result =0
for i in range(1,n+1):
    p = devi(i)
    if devi(p)==i and p!=i:
        result+=p+i
print(result/2)
