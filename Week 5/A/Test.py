import random

f = open("F.txt", "a")
test = 100
n = 16
t = 3600
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