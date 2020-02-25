

cache = {1: 1, 0: 0}

def get_chain_len(n):
    if n in cache:
        return cache[n]
    if n % 1000 == 0:
        print(">", n)
    if n % 2 == 0:
        l = 1 + get_chain_len(n // 2)
    else:
        l = 1 + get_chain_len(3 * n + 1)
    cache[n] = l
    return l

def argmax(func, arguments):
    best_out = float("-inf")
    best_inp = None
    for inp in arguments:
        out = func(inp)
        if out > best_out:
            best_out = out
            best_inp = inp
    return best_inp

print(argmax(get_chain_len, range(1_000_000)))