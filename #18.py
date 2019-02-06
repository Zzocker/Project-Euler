with open("#18.txt","r") as ins:
    raw_lis = []
    for line in ins:
        raw_lis.append(line.split(" "))
lis = []
for elm in raw_lis:
    lis.append(list(map(int,elm)))
print(lis)
net_lis = [[0 for i in range(len(lis[-1])) ]for j in range(len(lis))]
for i in range(len(net_lis)):
    for j in range(len(lis[i])):
        net_lis[i][j]=lis[i][j]
print(net_lis)
for i in range(len(net_lis)-2,-1,-1):
    for j in range(i+1):
        if net_lis[i+1][j]> net_lis[i+1][j+1]:
            net_lis[i][j]+=net_lis[i+1][j]
        else:
            net_lis[i][j] += net_lis[i + 1][j+1]
print(net_lis[0][0])