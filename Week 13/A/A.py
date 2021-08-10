import sys

squares = int(sys.stdin.readline())
fees = []
for i in range(squares):
    fees.append(int(sys.stdin.readline()))

position = 1
paid = fees[0] + fees[1]
lastjump = 1
nextstates = []


while(position != squares - 1):
    print(position, paid)

    if(position - lastjump < 0):
        position = position + lastjump + 1
        lastjump += 1
        paid += fees[position]

    elif(position + lastjump + 1 >= squares):
        position = position - lastjump
        paid += fees[position]

    elif(fees[position + lastjump + 1] < fees[position - lastjump]):
        position = position + lastjump
        lastjump += 1
        paid += fees[position]
    else:
        position = position - lastjump
        paid += fees[position]