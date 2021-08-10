import sys

def DFS(seen, children):
    while not all(seen):
        cycle = [False for _ in range(len(seen))]
        smallest_notseen = seen.index(False)
        stack = [smallest_notseen]
        seen[smallest_notseen] = True
        while len(stack) > 0:
            v = stack.pop()
            cycle[v] = True
            print(cycle, seen, v, children[v])
            for child in children[v]:
                if not seen[child]:
                    seen[child] = True
                    stack.append(child)
                if cycle[child]:
                    return False
    return True

def Kahn(parents, children, n):
    num_parents = [len(l) for l in parents]
    stack = [i for i in range(n) if num_parents[i] == 0]
    toposort = []

    while len(stack) > 0:
        cur = stack.pop()
        toposort.append(cur)
        for child in children[cur]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                stack.append(child)
    return toposort

firstline = sys.stdin.readline().split()
sticks = int(firstline[0])
lines = int(firstline[1])

parents = [[] for i in range(sticks)]
children = [[] for i in range(sticks)]
n = len(parents)
for i in range(lines):
    newline = sys.stdin.readline().split()
    parent = int(newline[0]) - 1
    child = int(newline[1]) - 1
    if(parent != child):


seen = [False for _ in range(len(children))]
if(DFS(seen, children) == True):
    gesorteerd = Kahn(parents, children, n)
    for i in range(len(gesorteerd)):
        print(gesorteerd[i] + 1)
else:
    print("IMPOSSIBLE")