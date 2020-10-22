

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input('input n to find primes: '))
for i in range(0, n):
    if isPrime(i):
        print(i, end=', ')
print()
