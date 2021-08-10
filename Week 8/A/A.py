import math

N = int(input())
prime = 1
if(N == 1):
    print(0)
else:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            print(N - int(N/i))
            prime = 0
            break
    if(prime == 1):
        print(N-1)