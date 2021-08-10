import math
while(True):
    priem = 0
    invoer = input().split()
    p = int(invoer[0])
    getal = int(invoer[1])
    a = getal
    if(p == 3):
        print("no")
        continue
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            break
        if i == int(math.sqrt(p)):
            priem = 1

    if(a == 0 and p == 0):
        break
    if(priem == 0):
        a = pow(a,p,p)
        if(a == getal):
            print("yes")
        else:
            print("no")
    else:
        print("no")