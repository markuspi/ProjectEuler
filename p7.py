
def is_prime(n):
    return all(n % d != 0 for d in range(2, 1 + int(n**0.5)))

primes = 0
n = 1
while primes < 10001:
    n += 1
    if is_prime(n):
        primes += 1
    
print(n)