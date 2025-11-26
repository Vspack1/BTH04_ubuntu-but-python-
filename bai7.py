import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhap mot so nguyen: "))
if isPrime(n):
    print(f"{n} la so nguyen to.")
else:
    print(f"{n} khong phai la so nguyen to.")