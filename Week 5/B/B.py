from collections import deque

def edge2adj_undirected(V, E, edges):
    adjlist = [[] for _ in range(V)]
    for (v, w) in edges:
        v = v
        w = w
        adjlist[v].append(w)
        adjlist[w].append(v)
    return adjlist

firstline = input().split()
secondline = input().split()
N = int(firstline[0])
H = int(firstline[1])
L = int(firstline[2])

vertices = [i for i in range(N)]
horror = []
for i in range(H):
    horror.append(int(secondline[i]))

edges = []
for i in range(L):
    invoer = input().split()
    edgefirst = int(invoer[0])
    edgelast = int(invoer[1])
    edges.append([edgefirst, edgelast])

nbs = edge2adj_undirected(N, L, edges)
start = 100000
score = [start for _ in range(len(nbs))]

for i in range(H):
    seen = [False for _ in range(len(nbs))]
    current = horror[i]
    queue = deque([current])
    score[current] = 0
    seen[current] = True
    while len(queue) > 0:
        v = queue.popleft()
        for nbr in nbs[v]:
            if(seen[nbr] == False):
                seen[nbr] = True
                if(score[v] + 1 < score[nbr]):
                    score[nbr] = score[v] + 1
                queue.append(nbr)

maxscore = 0
for i in range(N):
    if(score[i] > score[maxscore]):
        maxscore = i

print(maxscore)