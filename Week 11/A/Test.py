import random

f = open("A2.txt", "a")
n = 1000
m = 1000
print(n, m, file=f)

for i in range(m):
    x = random.randint(1,n)
    y = random.randint(1,n)

    while(x == y):
        y = random.randint(1, n)

    print(x, y, file=f)
f.close()