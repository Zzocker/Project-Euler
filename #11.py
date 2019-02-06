lis = []
for i in range(1,101):
    lis.append(i)
print(lis)
iter(lis)
for a,b,c in lis,lis,lis:
    if a<b<c and a+b+c==100 and a**2 +b**2 == c**2:
        print("%s, %s ,%s"%(a,b,c))
