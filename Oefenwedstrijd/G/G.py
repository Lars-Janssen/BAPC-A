targets = int(input())
locations = []
for i in range(targets):
    cors = input().split()
    xcor = int(cors[0])
    ycor = int(cors[1])
    locations.append([xcor, ycor])

lines = []
for i in range(targets):
    for y in range(i):
print(locations)