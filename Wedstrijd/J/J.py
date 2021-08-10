import sys
firstline = sys.stdin.readline().split()
members = int(firstline[0])
songs = int(firstline[1])

array = [[0 for i in range(songs)] for i in range(members)]
for i in range(members):
    newsong = sys.stdin.readline().split()
    for y in range(songs):
        array[i][y] = newsong[y]

testset = {array[0][0]}

for i in range(songs):
    for y in range(members):
        testset.add(array[y][i])
    if(len(testset) == i + 1):
        print(i+1)
        antwoord = list(testset)
        antwoord.sort()
        for i in range(len(antwoord)):
            print(antwoord[i], end = " ")
        sys.exit()