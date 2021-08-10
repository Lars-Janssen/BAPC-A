def edge2adj_undirected(V, E, edges):
    """ Given an undirected graph as a 1-based edge list,
    produce a 0-based adjacency list. """
    assert len(edges) == E
    adjlist = [[] for _ in range(V)]
    for (v, w) in edges:
        assert 1 <= v <= V and 1 <= w <= V
        v = v - 1
        w = w - 1
        adjlist[v].append(w)
        adjlist[w].append(v)
    return adjlist

firstline = input().split()
V = int(firstline[0])
E = int(firstline[1])
edges = []
for i in range(E):
    newEdge = input().split()
    for y in range(len(newEdge)):
        newEdge[y] = int(newEdge[y])
    edges.append(newEdge)
adjlist = edge2adj_undirected(V, E, edges)
seen = [False for _ in range(len(adjlist))]
stack = [0]
seen[0] = True
while len(stack) > 0:
    v = stack.pop()
    for nbr in adjlist[v]:
        if not seen[nbr]:
            seen[nbr] = True
            stack.append(nbr)

for i in range(len(seen)):
    if(seen[i] == False):
        print(i + 1)

if(all(seen)):
    print("Connected")