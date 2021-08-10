n = int(input())
stack = []
cards = [int(x) for x in input().split()]
for i in range(len(cards)):
    if(cards[i] % 2 == 0):
        stack.append(0)
    else:
        stack.append(1)
    if(len(stack) >= 2):
        last = stack.pop()
        second = stack.pop()
        if(last != second):
            stack.append(second)
            stack.append(last)
print(len(stack))