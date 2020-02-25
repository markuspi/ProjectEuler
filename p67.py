#!/usr/bin/env python3

with open("p18.txt") as f:
    triangle_p18 = [[int(n) for n in line.split(" ")] for line in f]

with open("p67.txt") as f:
    triangle_p67 = [[int(n) for n in line.split(" ")] for line in f]

def solve_triangle(triangle):
    # pad with zeros to avoid IndexError
    best = [0, 0]
    for row in triangle:
        best = [0] + [max(best[j:j+2]) + item for j, item in enumerate(row)] + [0]
    return max(best)

# let's play some code golf
import functools as c

def solve_triangle_v2(t):
    return max(c.reduce(lambda b,w:[0]+[max(b[j:j+2])+m for j,m in enumerate(w)]+[0],t,[0,0]))



print("p18:", solve_triangle_v2(triangle_p18))
print("p67:", solve_triangle_v2(triangle_p67))


print(max(c.reduce(lambda b,w:[0]+[max(b[j:j+2])+int(m)for j,m in enumerate(w.split())]+[0],open("p67.txt"),[0,0])))
