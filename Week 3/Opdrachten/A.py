vertices = int(input())
while(vertices != -1):
    edgetable = []
    for i in range(vertices):
        edgetable.append(input().split())
    for i in range(len(edgetable)):
        for y in range(len(edgetable)):
            edgetable[i][y] = int(edgetable[i][y])

    adj = []
    for y in range(vertices):
        adj.append([])
    for i in range(vertices):
        for y in range(vertices):
            if(edgetable[i][y] == 1):
                adj[i].append(y)
                
    weak = []
    for vertex in range(vertices):
        isWeak = True
        for othervertex in adj[vertex]:
            if(othervertex != vertex):
                for thirdvertex in adj[othervertex]:
                    if(thirdvertex != vertex and thirdvertex != othervertex and thirdvertex in adj[vertex]):
                        isWeak = False
        if(isWeak == True):
            weak.append(vertex)
    for i in range(len(weak)):
        if(i != len(weak) - 1):
            print(weak[i], end =" ")
        else:
            print(weak[i], end = "")
    print()

    vertices = int(input())