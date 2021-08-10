def edge2adj_undirected(V, E, edges):
    """ Given an undirected graph as a 1-based edge list,
    produce a 0-based adjacency list. """
    adjlist = [[] for _ in range(V)]
    for (v, w) in edges:
        v = v - 1
        w = w - 1
        adjlist[v].append(w)
        adjlist[w].append(v)
    return adjlist

def DFS(node):
    stack = [node]
    kleur[node] = 1
    cl = 1
    while(len(stack) > 0):
        v = stack.pop()
        for nbr in adjlist[v]:
            if not seen[nbr]:
                seen[nbr] = True
                kleur[nbr] = kleur[v] * -1
                stack.append(nbr)
                cl = cl + 1
    return cl

firstline = input().split()
construction = int(firstline[0])
walkways = int(firstline[1])
edges = []
for i in range(walkways):
    a, b = [int(x) for x in input().split()]
    edges.append([a,b])

adjlist = edge2adj_undirected(construction, walkways, edges)

stack = [0]
seen = [False for _ in range(construction)]
kleur = [0 for _ in range(construction)]
seen[0] = True
impossible = False
index = 0
while (index < construction):
    componentlength = DFS(index)
    if(componentlength == 1):
        print("Impossible")
        impossible = True
        break
    while(index < construction and seen[index] == True):
        index = index + 1

if(impossible == False):
    for i in range(construction):
        if(kleur[i] == 1):
            print("pub", end = ' ')
        else:
            print("house", end = ' ')