amount = int(input())
secondLine = input().split()
numbers = [int(secondLine[i]) for i in range(amount)]

ans = 0
changed = 1
while(changed == 1):
    changed = 0
    for i in range(amount):
        if(ans ^ numbers[i] > ans):
            ans = ans ^ numbers[i]
            changed = 1

print(ans)
