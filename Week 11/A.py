def kahn(parents, children):
    """ Performs Kahn's Algorithm given the incoming and outgoing adjlists. """
    n = len(parents)
    num_parents = [len(l) for l in parents]
    stack = [i for i in range(n) if num_parents[i] == 0]
    seen = [i for i in range(n) if num_parents[i] == 0]
    toposort = [] # will contain the toposort ordering
    while len(stack) > 0:
        cur = stack.pop()
        toposort.append(cur)
        for child in children[cur]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                if(child in seen):
                    return False
                stack.append(child)
                seen.append(child)
    while(0 in num_parents):
        num_parents.remove(0)
    if(len(num_parents) == 0):
        return toposort
    else:
        return False

def edgelist_to_adjlists(num_vertices, edgelist):
    incoming_adjlist = [[] for _ in range(num_vertices)]
    outgoing_adjlist = [[] for _ in range(num_vertices)]
    for i in range(len(edgelist)):
        incoming_adjlist[edgelist[i][1]].append(edgelist[i][0])
        outgoing_adjlist[edgelist[i][0]].append(edgelist[i][1])
    return incoming_adjlist, outgoing_adjlist

import sys
firstline = sys.stdin.readline().split()
vertices_num = int(firstline[0])
edges_num = int(firstline[1])

edges = []
for i in range(edges_num):
    edge = sys.stdin.readline().split()
    for y in range(len(edge)):
        edge[y] = int(edge[y]) - 1
    edges.append(edge)
parents, children = edgelist_to_adjlists(vertices_num, edges)

topo = kahn(parents, children)
if(topo == False):
    print("IMPOSSIBLE")
else:
    for i in range(len(topo)):
        print(topo[i] + 1)