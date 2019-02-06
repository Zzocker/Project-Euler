dic= {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
def word_sum(line):
    result = 0
    for alpha in line:
        result+=dic[alpha]
    return result

with open("name.txt","r") as ins:
    for line in ins:
        lis = line.split("\",\"")
lis=sorted(lis)
net = 0
for elm in lis:
    net+=word_sum(elm)*(lis.index(elm)+1)
print(net)



