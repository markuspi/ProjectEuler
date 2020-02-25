#!/usr/bin/env python3

import math

def count_factors(num):
    factors = 0
    sqrt = int(math.sqrt(num))
    for i in range(1, sqrt):
        if num % i == 0:
            factors += 2
    if sqrt ** 2 == num:
        factors += 1
    return factors


if __name__ == "__main__":    
    x = 0
    i = 0
    while True:
        i += 1
        x += i
        if i % 1000 == 0:
            print(i, x)
        if count_factors(x) > 500:
            print(">>>", x)
            break
