

def is_square(n):
    return int(n ** 0.5) ** 2 == n

def find_triplet(s):
    for b in range(1, 1000):
        for a in range(1, b):
            c_sq = a * a + b * b
            c = int(c_sq ** 0.5)
            if is_square(c_sq) and a + b + c == s:
                print(a, b, c, a * b * c)
                return a, b, c

find_triplet(1000)