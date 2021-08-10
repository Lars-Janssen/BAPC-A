import random

f = open("C.txt", "a")
n=100000
print(n, file=f)
for i in range(n):
    print(random.randint(0,n), file=f)
f.close()