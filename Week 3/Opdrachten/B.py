
def DFS(v, component, nbs):
    for nbr in nbs[v]:
        if component[nbr] == -1:
            component[nbr] = component[v]
            DFS(nbr, component, nbs)

cities = int(input())
for i in range(cities):
    vertices = int(input())
    edgenumber = int(input())
    adjecent = []
    for y in range(vertices):
        adjecent.append([])

    for y in range(edgenumber):
        newedge = input().split()
        newedge = [int(p) for p in newedge]
        adjecent[newedge[0]].append(newedge[1])
        adjecent[newedge[1]].append(newedge[0])

    num_components = 0
    component = [-1 for _ in range(len(adjecent))]
    for v in range(len(adjecent)):
        if component[v] == -1:
            component[v] = num_components
            num_components += 1
            DFS(v, component, adjecent)
    print(num_components - 1)