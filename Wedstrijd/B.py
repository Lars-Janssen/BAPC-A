import sys
from heapq import heappop, heappush
firstline = sys.stdin.readline().split()
cities = int(firstline[0])
roads = int(firstline[1])
flights = int(firstline[2])
start = int(firstline[3])
destination = int(firstline[4])

def relax(Fdist, dist, u, v, w):
    if(w == 0):
        if(Fdist[v] > dist[u] + w):
            Fdist[v] = dist[u] + w
            return True
    else:
        if(Fdist[v] > Fdist[u] + w):
            Fdist[v] = Fdist[u] + w
            dist[v] = Fdist[u] + w
            return True
        return False

def edgelist_to_adjlists(intersections, corridors, edges):
    adj = [[] for i in range(intersections)]
    for i in range(corridors):
        adj[edges[i][0]].append((edges[i][1], edges[i][2]))
        adj[edges[i][1]].append((edges[i][0], edges[i][2]))
    return adj

def Dijkstra(start, destination, V, adj):
    Q = []
    dist = [10**10 for u in range(V)]
    Fdist = [10**10 for u in range(V)]
    dist[start] = 0
    Fdist[start] = 0
    heappush(Q, (0, start))
    while len(Q):
        dist_u, u = heappop(Q)
        if(Fdist[u] < dist_u):
            continue
        if(u == destination):
            break
        for (v,w) in adj[u]:
            if(relax(Fdist, dist, u, v, w)):
                heappush(Q, (Fdist[v], v))
    return Fdist[destination]

adj = [[] for i in range(cities)]
for i in range(roads):
    newroad = sys.stdin.readline().split()
    adj[int(newroad[0])].append((int(newroad[1]),int(newroad[2])))
    adj[int(newroad[1])].append((int(newroad[0]),int(newroad[2])))

for i in range(flights):
    newflight = sys.stdin.readline().split()
    adj[int(newflight[0])].append((int(newflight[1]),0))

print(Dijkstra(start, destination, cities, adj))