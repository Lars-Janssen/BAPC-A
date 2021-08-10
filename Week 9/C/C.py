testcases = int(input())
def generate():
    walksto = [[[0 for i in range(20)] for i in range(20)] for i in range(20)]
    possiblewalks = [0 for i in range(20)]
    walksto[0][10][10] = 1
    for i in range(1, 20):
        for x in range(1, 19):
            for y in range(1, 19):
                walksto[i][x][y] = walksto[i-1][x+1][y] + walksto[i-1][x-1][y] + walksto[i-1][x][y+1] + walksto[i-1][x][y-1] + walksto[i-1][x-1][y+1] + walksto[i-1][x+1][y-1]
        possiblewalks[i] = walksto[i][10][10]
    return possiblewalks


walks = generate()
for i in range(testcases):
    n = int(input())
    print(walks[n])