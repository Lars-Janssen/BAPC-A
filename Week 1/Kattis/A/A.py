import math
x = int(input())
tests = []
count=0
while(count < x):
    tests.append(int(input()))
    count=count+1

for i in range(0,len(tests)):
    print(math.factorial(tests[i])%10)