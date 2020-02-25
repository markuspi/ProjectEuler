


rows = 20
cols = 20

cache = {}

def count_paths(x, y):
    if x == cols or y == rows:
        return 1
    key = (x, y)
    if key in cache:
        return cache[key]
    n = count_paths(x + 1, y) + count_paths(x, y + 1)
    cache[key] = n
    return n

print(count_paths(0, 0))