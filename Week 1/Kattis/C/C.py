amount = int(input())
n = []
counter = 0
while(counter < amount):
    counter = counter + 1
    n.append(input().lower())
    
for i in range(0,len(n)):
    missing = ""
    for y in range(ord('a'),ord('z')+1):
        if(chr(y) not in n[i]):
            missing = missing + chr(y)
    if(missing == ""):
        print("pangram")
    else:
        print("missing " + missing)