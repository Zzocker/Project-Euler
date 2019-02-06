dirt = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
dir2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
dir3 = ["hundred","thousand"]
def num_wor(n):
    if n in range(1,20):
        return len(dirt[n])
    if n in range(20,100):
        if str(n)[1]=="0":
            return len(dir2[int(str(n)[0])-2])
        else:
            return len(dir2[int(str(n)[0])-2]  + dirt[int(str(n)[1])])
    if n in range(100,1000):
        if str(n)[2]=="0" :
            if  str(n)[1]=="1":
                return len(dirt[int(str(n)[0])] + "hundredandten")
            elif str(n)[1]  not in ("0","1"):
                return len(dirt[int(str(n)[0])] + "hundredand" + dir2[int(str(n)[1]) - 2])
            elif str(n)[1] == "0":
                return len(dirt[int(str(n)[0])] + "hundred")
        else:
            if int(str(n)[1:3]) in range(1,20):
                return len(dirt[int(str(n)[0])] + "hundredand" +  dirt[int(str(n)[1:3])])
            if int(str(n)[1:3]) in range(20,100):
                return len(dirt[int(str(n)[0])] + "hundredand" + dir2[int(str(n)[1])-2] + dirt[int(str(n)[2])])
    if n==1000:
        return len("onethousand")
n= int(input())
m =0
for i in range(1,n+1):
    m+=num_wor(i)
print(m)