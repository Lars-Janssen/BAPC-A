import sys
from heapq import heappop, heappush

def edgelist_to_adjlists(nodes, edges, edgelist):
    adj = [[] for i in range(nodes)]
    for i in range(edges):
        adj[edgelist[i][0]].append((edgelist[i][1], edgelist[i][2]))
    return adj

def relax(dist, u, v, w):
    if(dist[v] > dist[u] + w):
        dist[v] = dist[u] + w
        return True
    return False

def Dijkstra(V, adj, source, target):
    Q = []
    dist = [10**10 for u in range(V)]
    dist[source] = 0
    heappush(Q, (0,source))
    while len(Q):
        dist_u, u = heappop(Q)
        if(u == target):
            break
        if(dist[u] < dist_u):
            continue
        for (v,w) in adj[u]:
            if(relax(dist, u, v, w)):
                heappush(Q, (dist[v], v))
    if(dist[target] != 10**10):
        return dist[target]
    else:
        return "Impossible"

while True:
    line = sys.stdin.readline().split()
    nodes = int(line[0])
    edges = int(line[1])
    queries = int(line[2])
    source = int(line[3])
    if(nodes == edges == queries == source == 0):
        break

    edgelist = []
    for i in range(edges):
        newedge = sys.stdin.readline().split()
        edgelist.append([int(newedge[0]), int(newedge[1]), int(newedge[2])])
    adj = edgelist_to_adjlists(nodes, edges, edgelist)
    print(adj)
    for i in range(queries):
        target = int(sys.stdin.readline())
        print(Dijkstra(nodes, adj, source, target))
    print()
