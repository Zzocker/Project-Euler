n = int(input())
result = pow(2,n)
m= 0
for digit in str(result):
    m+=int(digit)
print(m)
