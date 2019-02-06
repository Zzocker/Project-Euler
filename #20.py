from math import factorial as fac
n = fac(int(input()))
result = 0
for elm in str(n):
    elm = int(elm)
    result+=elm
print(result)