
f1 = 1
f2 = 1
s = 0

while True:
    fn = f1 + f2
    if fn % 2 == 0:
        s += fn
    
    if fn > 4000000:
        break

    f1 = f2
    f2 = fn

print(s)