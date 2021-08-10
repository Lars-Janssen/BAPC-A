import math
start = input().split()
pos1 = int(start[0])
pos2 = int(start[1])
pos3 = int(start[2])

biggestgap = max(pos2-pos1, pos3-pos2)
steps = biggestgap - 1
print(steps)