lis = []
for line in open("#13.txt", "r"):
    lis.append(line)
new_lis = []
for elm in lis:
    j = elm.split(" ")
    k = [int(n) for n in j]
    new_lis.append(k)
dg_lis = []
side_lis = []
up_lis = []
dg_lis2 = []
for i in range(17):
    for j in range(17):
        dg_lis.append(new_lis[i][j]*new_lis[i+1][j+1]*new_lis[i+2][j+2]*new_lis[i+3][j+3])
        side_lis.append(new_lis[i][19-j]*new_lis[i][18-j]*new_lis[i][17-j]*new_lis[i][16-j])
        up_lis.append(new_lis[19-i][j]*new_lis[18-i][j]*new_lis[17-i][j]*new_lis[16-i][j])
        dg_lis2.append(new_lis[i][j]*new_lis[i-1][j+1]*new_lis[i-2][j+2]*new_lis[i-3][j+3])
max_lis = [max(dg_lis2),max(dg_lis),max(up_lis),max(side_lis)]
print(max(max_lis))
