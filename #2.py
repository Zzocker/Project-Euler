n = 10
num = []
n1=0
n2=1
i=0
sum =0

while i in range(10000):
    nth = n1+n2
    n1=n2
    n2=nth
    if nth in range(4000000+1):
        if nth%2==0:
            sum = sum + nth
    else:
        break
    i=i+1
print(sum)
