from collections import deque
invoer = input()
counter = []
previous = ""
lastthree = deque([])
for i in range(len(invoer)):

    if(len(lastthree) >= 3):
        for y in range(3):
            counter.pop()
        counter.append("C")
        lastthree = deque([])

    if(invoer[i] == "R"):
        counter.append("S")
    if(invoer[i] == "B"):
        counter.append("K")
    if(invoer[i] == "L"):
        counter.append("H")

    while(invoer[i] in lastthree):
        lastthree.popleft()

    lastthree.append(invoer[i])


if(len(lastthree) >= 3):
    for y in range(3):
        counter.pop()
    counter.append("C")
    lastthree = deque([])

output = ""
for i in range(len(counter)):
    output= output + counter[i]
print(output)