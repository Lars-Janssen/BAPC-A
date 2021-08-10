while True:
    lijst1 = []
    lijst2 = []
    aantal = int(input())

    if(aantal == False):
        break
    else:
        print("")

    for i in range(aantal):
        lijst1.append(int(input()))
    for i in range(aantal):
        lijst2.append(int(input()))
    lijst3 = sorted(lijst1)
    lijst4 = [0] * len(lijst1)

    for i in range(len(lijst3)):
        for y in range(len(lijst1)):
            if(lijst3[i] == lijst1[y]):
                lijst4[y] = min(lijst2)
                lijst2.remove(min(lijst2))

    for i in range(len(lijst4)):
        print(lijst4[i])