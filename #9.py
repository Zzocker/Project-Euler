n = 2000000
def is_prime(n):
    if all(n%i!=0 for i in range(2,n)):
        return True
sum = 0
for i in range(3,n,2):
    if is_prime(i)==True:
        sum = sum + i
print(sum+2)