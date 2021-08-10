firstline = input().split()
sizes = int(firstline[0])
colours = int(firstline[1])

size = []
colour = []

spill = 0
for i in range(sizes):
    size.append(int(input()))
size.sort()
high = len(size)
low = 0
last = 0
for y in range(colours):
    colour.append(int(input()))
colour.sort()

for i in range(len(colour)):
    high = len(size)
    low = last
    currentColour = colour[i]
    while True:
        current = (high + low) // 2
        if(size[current] >= currentColour):
            if(current == 0 or size[current] == currentColour):
                spill += size[current] - currentColour
                last = current
                break
            elif(size[current - 1] < currentColour):
                spill += size[current] - currentColour
                last = current
                break
            else:
                high = current
        else:
            low = current

print(spill)