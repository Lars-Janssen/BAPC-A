import sys
from heapq import heappop, heappush

def edgelist_to_adjlists(intersections, corridors, edges):
    adj = [[] for i in range(intersections)]
    for i in range(corridors):
        adj[edges[i][0]].append((edges[i][1], edges[i][2]))
        adj[edges[i][1]].append((edges[i][0], edges[i][2]))
    return adj

def relax(dist, u, v, w):
    if(dist[v] < dist[u] * w):
        dist[v] = dist[u] * w
        return True
    return False

def Dijkstra(V, adj):
    Q = []
    dist = [0 for u in range(V)]
    dist[0] = 1
    heappush(Q, (-1,0))
    while len(Q):
        dist_u, u = heappop(Q)
        dist_u = -dist_u
        if(u == V-1):
            break
        if(dist[u] > dist_u):
            continue
        for (v,w) in adj[u]:
            if(relax(dist, u, v, w)):
                heappush(Q, (-dist[v], v))
    return dist[-1]

while(True):
    firstline = sys.stdin.readline()
    if(firstline != ""):
        firstline = firstline.split()
        intersections = int(firstline[0])
        corridors = int(firstline[1])
        if(intersections == 0 and corridors == 0):
            continue
        else:
            edges = []
            for i in range(corridors):
                newedge = sys.stdin.readline().split()
                edges.append([int(newedge[0]), int(newedge[1]), float(newedge[2])])
            adj = edgelist_to_adjlists(intersections, corridors, edges)
            print('{0:.4f}'.format(Dijkstra(intersections, adj)))

    else:
        break