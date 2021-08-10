import sys

def edgelist_to_adjlists(num_vertices, edgelist):
    incoming_adjlist = [[] for _ in range(num_vertices)]
    outgoing_adjlist = [[] for _ in range(num_vertices)]
    for i in range(len(edgelist)):
        incoming_adjlist[edgelist[i][1]].append(edgelist[i][0])
        outgoing_adjlist[edgelist[i][0]].append(edgelist[i][1])
    return incoming_adjlist, outgoing_adjlist

def kahn(parents, children):
    """ Performs Kahn's Algorithm given the incoming and outgoing adjlists. """
    n = len(parents)
    assert n == len(children)
    num_parents = [len(l) for l in parents]
    stack = [i for i in range(n) if num_parents[i] == 0]
    toposort = [] # will contain the toposort ordering

    while len(stack) > 0:
        cur = stack.pop()
        toposort.append(cur)
        for child in children[cur]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                stack.append(child)
    return toposort

firstline = sys.stdin.readline().split()
metals = int(firstline[0])
experiments = int(firstline[1])

edges = []
for i in range(experiments):
    result = sys.stdin.readline().split()
    parent = int(result[0])
    child = int(result[1])
    edges.append([parent, child])

parents, children = edgelist_to_adjlists(metals, edges)

toposort = kahn(parents, children)
unique = True
for i in range(len(toposort) - 1):
    if([toposort[i], toposort[i+1]] not in edges):
        print("back to the lab")
        unique = False

if(unique == True):
    for i in range(len(toposort)):
        print(toposort[i], end = ' ')

