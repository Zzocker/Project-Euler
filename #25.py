index = 1
a= 0
b= 1
result =0
n = int(input("Number of Digit : "))
while True:
    result=a+b
    a=b
    b=result
    index+=1
    if len(str(result))==n:
        print(index)
        break




