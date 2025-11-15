#funkcija isPrime()
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(isPrime(7))
print(isPrime(19))

#funckija prime_in_range()
def primes_in_range(start, end):
    prosti = []
    for broj in range(start, end + 1):
        if isPrime(broj):
            prosti.append(broj)
    return prosti
print(primes_in_range(1, 10))

