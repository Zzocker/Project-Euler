n = int(input())
lis = []
result = 0
for a in range(2,n+1):
    for b in range(2,n+1):
        if a**b not in lis:
            lis.append(a**b)
            result+=1
print(result)


