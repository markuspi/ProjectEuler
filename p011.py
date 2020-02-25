
import numpy as np

def range2(a, b):
    for i in range(a):
        for j in range(b):
            yield i, j

grid = np.loadtxt('p11.txt', dtype="int")

hori = max(grid[i+0,j+0]*grid[i+1,j+0]*grid[i+2,j+0]*grid[i+3,j+0] for i,j in range2(17, 20))
vert = max(grid[i+0,j+0]*grid[i+0,j+1]*grid[i+0,j+2]*grid[i+0,j+3] for i,j in range2(20, 17))
dia1 = max(grid[i+0,j+0]*grid[i+1,j+1]*grid[i+2,j+2]*grid[i+3,j+3] for i,j in range2(17, 17))
dia2 = max(grid[i+3,j+0]*grid[i+2,j+1]*grid[i+1,j+2]*grid[i+0,j+3] for i,j in range2(17, 17))

print(max(hori, vert, dia1, dia2))