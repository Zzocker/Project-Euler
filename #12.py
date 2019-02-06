n = int(input())
lis = []
len = 0
lis3 = []
for i in range(n):
    word = input()
    lis.append(word)
    if word not in lis:
        len+=1
for elm in lis:
    lis3.append(lis.count(elm))
print(len)
print(*lis3,sep=" ")

