import sys

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
metals = int(firstline[0])
experiments = int(firstline[1])

if(experiments < metals - 1):
    print("back to the lab")
    sys.exit()

parents = [[] for i in range(metals)]
children = [[] for i in range(metals)]
n = len(parents)

for i in range(experiments):
    newline = sys.stdin.readline().split()
    parent = int(newline[0])
    child = int(newline[1])
    parents[child].append(parent)
    children[parent].append(child)

toposort = Kahn(parents, children, n)
startpoint = 0
components = []
for i in range(len(toposort)):
    if(i == len(toposort) - 1):
        components.append(toposort[startpoint:i+1])
        break
    elif(toposort[i+1] not in children[i]):
        components.append(toposort[startpoint:i+1])
        startpoint = i + 1
print(components)
if(len(components) == 1):
    for i in range(len(toposort)):
        print(toposort[i])