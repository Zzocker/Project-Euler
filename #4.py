lis = []
p=0
for i in range(100,1000):
    for j in range(10,1000):
        n = i*j
        n = str(n)
        if i*j in range(100000,999999) and i<=j and n[0]==n[5]and n[1]==n[4] and n[2]==n[3]:
            lis.append(n)
            p=p+1
print(max(lis))