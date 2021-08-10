firstline = input().split()
molecule = input()
have = firstline[0]
amount = int(firstline[1])
havelist = [char for char in have]
moleculelist = [char for char in molecule]


atoms = []
amounts = []
atomsNeeded = []
amountsNeeded = []
i = 0
while i < (len(havelist)):
    newatom = havelist[i]
    j = i + 1
    number = ""
    while(j < len(havelist) and havelist[j].isdigit()):
        number += havelist[j]
        j += 1
    if(number == ""):
        number = 1
    else:
        number = int(number)
    atoms.append(newatom)
    amounts.append(number)
    i = j

i = 0
while i < (len(moleculelist)):
    newatom = moleculelist[i]
    j = i + 1
    number = ""
    while(j < len(moleculelist) and moleculelist[j].isdigit()):
        number += moleculelist[j]
        j += 1
    if(number == ""):
        number = 1
    else:
        number = int(number)
    atomsNeeded.append(newatom)
    amountsNeeded.append(number)
    i = j

print(atoms)
print(amounts)
print(atomsNeeded)
print(amountsNeeded)

lastchanged = 10**10
while lastchanged != 0:
    for i in range(len(atomsNeeded)):
        atomNeeded = atomsNeeded[i]
        amountNeeded = amountsNeeded[i]
        print(atoms.index(atomNeeded))
