def isprim(n):
    sum=0
    for i in range(2,n):
        if(n%i==0):
            sum+=1
            break
    if (sum==0):
        return True
    else:
        return False
result =2
for i in range(3,2000000,2):
    if (isprim(i)==True):
        result+=result
print(result)

