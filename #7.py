def is_prim(n):
    if all(n%i!=0 for i in range(2,n)):
        return True
lis =[]
for j in range(3,200000,2):
    if is_prim(j):
        lis.append(j)
print(lis[9999])