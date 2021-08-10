import random

f = open("D.txt", "a")
n = 100000
m = 100000
print(n, m, file=f)
for i in range(n - 1):
    print(random.randint(1,1000), file=f)
print(1000, file=f)
for i in range(m):
    print(random.randint(1,1000), file=f)
f.close()