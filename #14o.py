def seq(n):
    m = 0
    while True:

        if n%2==0:
            n=n/2
            m+=1
        else:
            n=3*n+1
            m+=1
        if n==1:
            return m+1
            break
lis = []
lis2 = []
for num in range(2,1000001):
    lis.append(seq(num))
print(lis.index(max(lis))+2)
