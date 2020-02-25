

def is_prime(n):
    return all(n % d != 0 for d in range(2, 1 + int(n**0.5)))


print(sum(i for i in range(2, 2_000_000) if is_prime(i)))