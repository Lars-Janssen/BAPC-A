

N = int(input())
counter = 0
for y in range(0, N-1):
    i = N-1-y
    counter+= 1
    if(N % i == 0):
        break
print(counter)