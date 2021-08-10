import random

f = open("A2.txt", "a")
n = 5
m = 7
print(n, m, file=f)
edges = []
for i in range(m):
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    z = round(random.random(),1)

    while(x == y or (x,y) in edges or (y,x) in edges):
        y = random.randint(1, n-1)
    edges.append((x,y))
    print(x, y, z, file=f)
f.close()