from collections import deque
testcases = int(input())
for i in range(testcases):
    firstline = input().split()
    buttons_amount = int(firstline[0])
    time = int(firstline[1])
    buttons = input().split()
    buttons = [int(i) for i in buttons]

    times = [0]
    dist = [0]
    queue = deque([0])
    while len(queue) > 0:
        v = queue.popleft()
        for nbr in buttons:
            getal = v + nbr
            if(getal < 0):
                getal = 0
            if(getal > 3600):
                getal = 3600
            if(getal not in times):
                times.append(getal)
                queue.append(getal)
                dist.append(dist[times.index(v)] + 1)

    mintime = 3600
    for j in times:
        if(time <= j < mintime):
            mintime = j
    print(dist[times.index(mintime)], mintime - time)

