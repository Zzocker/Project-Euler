n = 100
num_lis = []
sq_sum = 0
for i in range(1,n+1):
    num_lis.append(i)
    sq_sum=sq_sum+i
sq_sum = pow(sq_sum,2)
sq_lis = []
for elm in num_lis:
    sq_lis.append(pow(elm,2))
sum1 = 0
for j in range(n):
    sum1=sum1+sq_lis[j]
print(sq_sum-sum1)