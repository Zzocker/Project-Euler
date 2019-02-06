lis = []
for line in open("#15.txt", "r"):
    lis.append(line)
new_lis = []
for elm in lis:
    new_lis.append(int(elm))
print(str(sum(new_lis))[0:10])


