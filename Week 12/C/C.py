import sys
from heapq import heappop, heappush

firstline = sys.stdin.readline().split()
length = int(firstline[0])
width = int(firstline[1])

def relax(dist, u, v, w):
    if(dist[v] > max(w, dist[u])):
        dist[v] = max(w, dist[u])
        return True
    return False

def Dijkstra(V, adj, source, target):
    Q = []
    dist = [10**10 for u in range(V)]
    dist[source] = 0
    heappush(Q, (source, 0))
    while len(Q):
        dist_u, u = heappop(Q)
        if(dist[u] < dist_u):
            continue
        for (v,w) in adj[u]:
            if(relax(dist, u, v, w)):
                heappush(Q, (dist[v], v))
    return dist[target]

heightlist = []
for i in range(length):
    newrow = sys.stdin.readline().split()
    for y in range(width):
        heightlist.append(int(newrow[y]))

adj = [[] for i in range(length * width)]
for i in range(length):
    for y in range(width):
        height = heightlist[i * width + y]
        if(i > 0):
            adj[i * width + y].append(((i-1) * width + y, heightlist[(i-1) * width + y] - height))
        if(i < length - 1):
            adj[i * width + y].append(((i+1) * width + y, heightlist[(i+1) * width + y] - height))
        if(y > 0):
            adj[i * width + y].append((i * width + y - 1, heightlist[i * width + y - 1] - height))
        if(y < width - 1):
            adj[i * width + y].append((i * width + y + 1, heightlist[i * width + y + 1] - height))

for i in range(length):
    for y in range(width):
        for u in range(len(adj[i * width + y])):
            if(adj[i * width + y][u][1] < 0):
                adj[i * width + y][u] = (adj[i * width + y][u][0], 0)

print(Dijkstra(length * width, adj, 0, length * width - 1))

