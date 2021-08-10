papers = int(input())
citations = []
for i in range(papers):
    citations.append(int(input()))

def citation(current):
    atleast = 0
    for y in range(len(citations)):
            if(citations[y] >= current):
                atleast = atleast + 1
    if(atleast >= current):
        return True
    else:
        return False

high = max(citations)
low = min(citations)
while(True):
    if(low > papers):
        print(papers)
        break

    current = (high+low) // 2
    if(low == high):
        print(current)
        break

    if(citation(current) == True and citation(current + 1) == False):
        print(current)
        break
    elif(citation(current) == True and citation(current + 1) == True):
        if(low == current):
            print(current + 1)
            break
        low = current
    elif(citation(current) == False):
        high = current



