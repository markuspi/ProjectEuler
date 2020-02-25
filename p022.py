
def word_score(word):
    return sum(ord(c) - 64 for c in word)

with open("p22_names.txt") as f:
    data = "[" + f.read() + "]"
    names = sorted(eval(data))

total = 0
for i, name in enumerate(names):
    total += (i + 1) * word_score(name)

print(total)