import random

f = open("F.txt", "a")
M = 2000000000
N = 100000
sUm = 0
numbers = [0] * N
print(M, N, file=f)
while(sUm <= M):
    sUm = 0
    for i in range(N):
        numbers[i] = random.randint(0,M)
        sUm = sUm + numbers[i]

for i in range(N):
    print(numbers[i], file=f)
f.close()