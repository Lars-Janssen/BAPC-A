from collections import deque
firstline = input().split()
n = int(firstline[0])
m = int(firstline[1])
grid = []
for i in range(n):
    line = input()
    chars = [char for char in line]
    for j in range(m):
        grid.append(int(chars[j]))

nbs = [[] for _ in range(n*m)]
for i in range(n):
    for j in range(m):
        value = grid[i*m + j]
        if(value == 0):
            continue
        if(0 <= i + value < n):
            nbs[i*m+j].append((i+value)*m+j)
        if(0 <= i - value < n):
            nbs[i*m+j].append((i-value)*m+j)
        if(0 <= j + value < m):
            nbs[i*m+j].append(i*m+(j+value))
        if(0 <= j - value < m):
            nbs[i*m+j].append(i*m+(j-value))

dist = [-1 for _ in range(len(nbs))]
queue = deque([0])
dist[0] = 0
while len(queue) > 0:
    v = queue.popleft()
    for nbr in nbs[v]:
        if dist[nbr] == -1:
            dist[nbr] = dist[v] + 1
            queue.append(nbr)

print(dist[n*m - 1])