
from collections import Counter

all_pf = Counter()

def prime_factors(n):
    pf = Counter()
    d = 2
    while d*d <= n:
        while n % d == 0:
            pf[d] += 1
            n //= d
        d += 1
    if n > 1:
        pf[n] += 1
    return pf

for i in range(2, 21):
    pf = prime_factors(i)
    for k, v in pf.items():
        all_pf[k] = max(v, all_pf[k])

result = 1
for k, v in all_pf.items():
    result *= k ** v
print(result)