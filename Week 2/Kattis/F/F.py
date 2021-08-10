firstline = input().split()
candy = int(firstline[0])
children = int(firstline[1])

wants = []
for i in range(children):
    wants.append(int(input()))
wants.sort()

y = 0
while(candy > 0):
    candy = candy - (wants[0]-wants[1])
    wants.sort()
    print(candy)

anger = 0
for i in range(len(wants)):
    anger = anger + (wants[i]*wants[i])
print(anger)