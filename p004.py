largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        p_str = str(p)
        if p_str == p_str[::-1] and p > largest:
            largest = p
print(largest)